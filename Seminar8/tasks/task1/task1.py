import matplotlib.pyplot as plt
import numpy as np
import cupy as cp

N = 1024

blur_kernel = cp.RawKernel(r'''

extern "C" __global__

void blur(float* img_vec, float* img_result_vec, size_t length, size_t height) {
	
	int i = 0, j = 0, n = 3;

	size_t s_idx;
	size_t global_block_index =	blockIdx.x + \
								blockIdx.y * gridDim.x + \
								blockIdx.z * gridDim.x * gridDim.y;
	
	size_t tid_in_block =		threadIdx.x + \
								threadIdx.y * blockDim.x + \
								threadIdx.z * blockDim.x * blockDim.y;
	
	size_t global_idx = 		tid_in_block + global_block_index * \
                        		blockDim.x * blockDim.y * blockDim.z;

    if (global_idx == 0){ // left up angle
    	s_idx = global_idx;
    	for (i = 0; i < n - 1; i++){
   			for(j = 0; j < n - 1; j++){
   				img_result_vec[global_idx] += img_vec[s_idx+j];
   			}
   			s_idx += length;
   		}
   		img_result_vec[global_idx] *= 1.0/((n - 1) * (n - 1));
    }else if (global_idx == length - 1){ // right up angle 
    	s_idx = global_idx - 1;
    	for (i = 0; i < n - 1; i++){
   			for(j = 0; j < n - 1; j++){
   				img_result_vec[global_idx] += img_vec[s_idx+j];
   			}
   			s_idx += length;
   		}
   		img_result_vec[global_idx] *= 1.0/((n - 1) * (n - 1));
    }else if (global_idx == (length * height - 1) - (length - 1)){ //left down angle
    	s_idx = global_idx - length;
    	for (i = 0; i < n - 1; i++){
   			for(j = 0; j < n - 1; j++){
   				img_result_vec[global_idx] += img_vec[s_idx+j];
   			}
   			s_idx += length;
   		}
   		img_result_vec[global_idx] *= 1.0/((n - 1) * (n - 1));
    }else if (global_idx == length * height - 1){ //right down angle
    	s_idx = global_idx - length - 1;
    	for (i = 0; i < n - 1; i++){
   			for(j = 0; j < n - 1; j++){
   				img_result_vec[global_idx] += img_vec[s_idx+j];
   			}
   			s_idx += length;
   		}
   		img_result_vec[global_idx] *= 1.0/((n-1)*(n-1));
    }else if ((global_idx)%length == 0){ // left border
    	s_idx = global_idx - length;
    	for (i = 0; i < n; i++){
   			for(j = 0; j < n - 1; j++){
   				img_result_vec[global_idx] += img_vec[s_idx+j];
   			}
   			s_idx += length;
   		}
   		img_result_vec[global_idx] *= 1.0/((n - 1) * n);
    }else if ((global_idx + 1)%length == 0){ // right border
    	s_idx = global_idx - length - 1;
    	for (i = 0; i < n; i++){
   			for(j = 0; j < n - 1; j++){
   				img_result_vec[global_idx] += img_vec[s_idx+j];
   			}
   			s_idx += length;
   		}
   		img_result_vec[global_idx] *= 1.0/((n - 1) * n);
    }else if (global_idx < length){ // up border
    	s_idx = global_idx - 1;
    	for (i = 0; i < n - 1; i++){
   			for(j = 0; j < n; j++){
   				img_result_vec[global_idx] += img_vec[s_idx+j];
   			}
   			s_idx += length;
   		}
   		img_result_vec[global_idx] *= 1.0/((n - 1) * n);
    }else if (global_idx > (length * height - 1) - length){ //down border
    	s_idx = global_idx - length - 1;
    	for (i = 0; i < n - 1; i++){
   			for(j = 0; j < n; j++){
   				img_result_vec[global_idx] += img_vec[s_idx+j];
   			}
   			s_idx += length;
   		}
   		img_result_vec[global_idx] *= 1.0/((n - 1) * n);
   	}else{
   		s_idx = global_idx - int(n/2) - length;
   		for (i = 0; i < n; i++){
   			for(j = 0; j < n; j++){
   				img_result_vec[global_idx] += img_vec[s_idx+j];
   			}
   			s_idx += length;
   		}
   		img_result_vec[global_idx] *= 1.0/(n * n);
   	}
}

''', 'blur')

def d_random_matrix_generator(ntuple):
    d_ndarray = cp.random.sample(ntuple)    
    return d_ndarray.astype(cp.single)

def d_blur(d_image):
	d_image_copy = d_image.copy()

	ege = 0	

d_image = d_random_matrix_generator((N,N))
d_image_vec = d_image.reshape(N*N)
h_image = d_image.get()
fig1 = plt.imshow(h_image, cmap = 'hot', extent = (0, N, 0, N))
plt.show()
d_image_copy = d_image.copy()
d_image_copy_vec = d_image_copy.reshape(N*N)

blur_kernel((N//32,N//32,), (32,32,), (d_image_vec, d_image_copy_vec, N, N))
d_image_copy = d_image_copy.reshape(N,N)
fig2 = plt.imshow(d_image_copy.get(), cmap = 'hot', extent = (0, N, 0, N))
plt.show()





from ipykernel.kernelapp import IPKernelApp
from . import BasilispKernel

IPKernelApp.launch_instance(kernel_class=BasilispKernel)

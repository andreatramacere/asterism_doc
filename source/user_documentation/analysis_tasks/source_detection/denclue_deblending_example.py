"""

"""

from asterism import data_dir
from asterism.core.image_manager.image import Image
from asterism.analysis_tasks.source_detection.background_estimation.background_estimation import DoSetBkgThreshTask
from asterism.analysis_tasks.source_detection.image_segmentation.image_segmentation import DoImageSegmentationTask
from asterism.analysis_tasks.source_detection.deblending.denclue_deblending import DoDENCLUEDeblendingTask
import  numpy as np

image=Image.from_fits_file(data_dir+'/deblending_img1.fits')

bkg_task=DoSetBkgThreshTask()
bkg_task.list_parameters()
bkg_task.set_par('plot',value=False)
bkg_task.set_par('skewness_range',value=0.1)
bkg_task.set_par('sub_block_frac_size',value=0.1)

bkg_threshold,bkg_mode,bkg_sig=bkg_task.run(image=image)

print bkg_threshold,bkg_mode,bkg_sig
image_seg_task=DoImageSegmentationTask()
image_seg_task.list_parameters()
image_seg_task.set_par('bkg_threshold',value=float(bkg_threshold))
image_seg_task.set_par('K',value=1.5)
image_seg_task.set_par('K_pix',value=True)
image_seg_task.set_par('plot_dbscan',value=True)

image_seg_task.list_parameters()

clusters_list,K,selected_coords=image_seg_task.run(image=image)

deblendig=DoDENCLUEDeblendingTask()
deblendig.list_parameters()
deblendig.set_par('do_denclue_deblending',value=True)
deblendig.set_par('gl_downsampling',value=False)
deblendig.set_par('h_frac',value=0.1)
deblendig.set_par('plot',value=True)
deblendig.set_par('verbose',value=True)


deblendig.run(clusters_list=clusters_list)

from asterism import data_dir
from asterism.core.image_manager.image import Image
from asterism.analysis_tasks.source_detection.background_estimation.background_estimation import set_thresh
from asterism.analysis_tasks.source_detection.image_segmentation.image_segmentation import do_image_segmentation
from asterism.analysis_tasks.source_detection.deblending.denclue_deblending import do_denclue_deblending

image=Image.from_fits_file(data_dir+'/deblending_img1.fits')
bkg_threshold,bkg_mode,bkg_sig=set_thresh(image,sub_block_frac_size=0.1,skewness_range=0.1,plot=False)
clusters_list,K,selected_coords=do_image_segmentation(image,bkg_threshold,K=np.float_(1.5),K_pix=True,plot_dbscan=True)
do_denclue_deblending(clusters_list=clusters_list,do_denclue_deblending=True,gl_downsampling=True,h_frac=0.1,plot=True)
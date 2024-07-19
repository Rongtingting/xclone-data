import xclone
xclone.pp.efficiency_preview()
import numpy as np
import sys

dataset_name = sys.argv[1]
## input dir
rdr_data_dir = sys.argv[2]
baf_data_dir = sys.argv[3]


## output dir
out_dir = sys.argv[4]

cell_anno_file = sys.argv[5]
anno_file_sep = sys.argv[6]
barcodes_key = sys.argv[7]

cell_anno_key = sys.argv[8]
ref_celltype = sys.argv[9]

## pre-check
xp_config = xclone.PreprocessingConfig(dataset_name = dataset_name, module = "pre_check", 
                                       rdr_data_dir = rdr_data_dir, baf_data_dir = baf_data_dir)
xp_config.display()
xclone.pp.load_Xdata(module = "pre_check",  config_file = xp_config)

## load data
### rdr
xp_config = xclone.PreprocessingConfig(dataset_name = dataset_name, module = "RDR",
                                       barcodes_key = barcodes_key,
                                       anno_file_sep = anno_file_sep,
                                       rdr_data_dir = rdr_data_dir)
xp_config.genome_mode = "hg38_genes"
xp_config.cell_anno_file = cell_anno_file
xp_config.cell_anno_key = cell_anno_key
xp_config.display()

RDR_adata = xclone.pp.load_Xdata(module = "RDR", config_file = xp_config)

### baf
xp_config = xclone.PreprocessingConfig(dataset_name = dataset_name, module = "BAF", 
                                       barcodes_key = barcodes_key,
                                       anno_file_sep = anno_file_sep,
                                       baf_data_dir = baf_data_dir)
xp_config.genome_mode = "hg38_genes"
xp_config.cell_anno_file = cell_anno_file
xp_config.cell_anno_key = cell_anno_key
xp_config.display()

BAF_adata = xclone.pp.load_Xdata(module = "BAF", 
            config_file = xp_config)




## RDR module
xconfig = xclone.XCloneConfig(
    dataset_name = dataset_name, 
    module = "RDR"
)

xconfig.set_figure_params(xclone= True, fontsize = 18)
xconfig.outdir = out_dir
xconfig.cell_anno_key = cell_anno_key
xconfig.ref_celltype = ref_celltype
xconfig.top_n_marker = 25
xconfig.marker_group_anno_key = cell_anno_key
xconfig.xclone_plot= True
xconfig.plot_cell_anno_key = cell_anno_key
xconfig.trans_t = 1e-6
xconfig.start_prob = np.array([0.3, 0.4, 0.3])
xconfig.display()

RDR_Xdata = xclone.model.run_RDR(RDR_adata, config_file = xconfig)


## BAF module
xconfig = xclone.XCloneConfig(dataset_name = dataset_name, module = "BAF")
xconfig.set_figure_params(xclone = True, fontsize = 18)
xconfig.outdir = out_dir
xconfig.cell_anno_key = cell_anno_key
xconfig.ref_celltype = ref_celltype
xconfig.plot_cell_anno_key = cell_anno_key
xconfig.phasing_region_key = "chr"
xconfig.BAF_denoise = True
xconfig.display()

BAF_merge_Xdata = xclone.model.run_BAF(BAF_adata, config_file = xconfig)



## Combine module
xconfig = xclone.XCloneConfig(dataset_name = dataset_name, module = "Combine")
xconfig.set_figure_params(xclone = True, fontsize = 18)
xconfig.outdir = out_dir
xconfig.cell_anno_key = cell_anno_key
xconfig.ref_celltype = ref_celltype
xconfig.xclone_plot= True
xconfig.plot_cell_anno_key = cell_anno_key
xconfig.merge_loss = False
xconfig.merge_loh = True
xconfig.BAF_denoise = True
xconfig.display()



combine_Xdata = xclone.model.run_combine(
    RDR_Xdata,
    BAF_merge_Xdata,
    verbose = True,
    run_verbose = True,
    config_file = xconfig
)
The latexeditor module works in the following fashion:  
1) we have template-repo (which we get from the internet).  
2) we then take we segment from the template and add those to a `./templates/temp_name/segment_name.py`.  
3) our ai resume editor uses the segment_module through accessing `main.py` which internally utilizes `template_manager.py`.  
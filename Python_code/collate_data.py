import os
import glob

import pandas as pd
import numpy as np

def collate_data(top_data_folder, summary_file_string,
                 max_sims_per_file = 100,
                 sim_file_path = 'sim_output',
                 sim_file_root = 'sim_prot*.*',
                 time_label = 'time',
                 keep_labels = ['hs_1_pCa', 'hs_1_length', 'hs_1_force']):
    """ Stores selected data columns from each summary file in
        a file. If there are more than max_sims_per_file, create
        a sequence of files with max_sims_per_file in each one """
    
    search_string = os.path.join(top_data_folder,
                                 '**',
                                 sim_file_path,
                                 '**',
                                 sim_file_root)
    
    sim_files = glob.glob(search_string, recursive=True)

    # Cycle through the files
    sim_file_counter = 1
    summary_file_counter = 1
    loop_file_counter = 1

    for (sim_file_i, sfs) in enumerate(sim_files):

        # Open the sim_file
        d_sim = pd.read_csv(sfs, sep='\t')
    
        if (loop_file_counter == 1):
            col_list = [d_sim['time']]
            col_labels = ['time']

        # Add the other columns
        for (ci, k_lab) in enumerate(keep_labels):
            new_lab = 'sim_%i_%s' % ((sim_file_i + 1),
                                     k_lab.split('_')[-1])
            
            # Transform Ca
            if (k_lab == 'hs_1_pCa'):
                d_sim[k_lab] = np.power(10, -d_sim[k_lab])

            # Add to arrays
            col_list.append(d_sim[k_lab])
            col_labels.append(new_lab)

        # Increment the counter
        loop_file_counter = loop_file_counter + 1

        # Write output file if required
        if ( (loop_file_counter == (max_sims_per_file + 1)) or
                (sim_file_i == (len(sim_files) - 1)) ):
            
            # Make the dataframe
            df = pd.concat(col_list, axis=1)
            df.columns = col_labels

            print(df)

            # Write file
            output_file_string = '%s_part_%i.txt' % \
                (summary_file_string, summary_file_counter)
            # Display
            print('Writing data to: %s' % output_file_string)
            df.to_csv(output_file_string, sep='\t', index=False)

            # Reset
            summary_file_counter = summary_file_counter + 1
            loop_file_counter = 1
            del col_list
            del col_labels

if __name__ == "__main__":
    """ Run code """

    top_data_folder = [
        '../simulations/n_vars_1',
        '../simulations/n_vars_3']
    
    summary_file_string = [
        '../simulations/summaries/summary_n_vars_1',
        '../simulations/summaries/summary_n_vars_3']
    
    for (i, temp) in enumerate(top_data_folder):
        collate_data(top_data_folder[i],
                     summary_file_string[i])

    
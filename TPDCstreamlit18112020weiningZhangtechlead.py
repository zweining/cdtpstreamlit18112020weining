import os
import streamlit as st
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib 
matplotlib.use('Agg') #Ce code peut afficher le graphique sans service GUI sous Linux
import seaborn as sns 
import tkinter.filedialog
import numpy as np
from threading import Event

#st.write(dir=input("Veuillez entrer le dossier où se trouve le fichier de données csv"))
def main():
    st.title("App de Dataset Explorer")
    st.subheader("construire une petite application de visualisation interactive de données avec l’outil Streamlit")
    html_temp='''
    <div style="background-color:tomato;"><p style="color:white;font-size:50px;">Streamlit data app</p></div>
    '''
    st.markdown(html_temp,unsafe_allow_html=True)
    
    st.text("Charger des jeux de données présents dans votre répertoire local↓")
    #if st.button("choisir une répertoire local"):
        #dir1=input("shuur")
     #   dir1=tkinter.filedialog.askdirectory( title='Veuillez ouvrir un dossier pour stocker les fichiers de données')
      #  st.write(dir1)
    #st.write(dir=input("Veuillez entrer le dossier où se trouve le fichier de données csv"))
   
    dir=st.text_input("Veuillez entrer le chemin du dossier où se trouve le fichier de données csv",".")  
    #dir=tkinter.filedialog.askdirectory( title='zifuchuan')
    
    
    try:

    #dir='D:/datasett/wenjiajia'
	    def file_selector(folder_path=dir):
	        filenames=os.listdir(folder_path)
	        selected_filename=st.selectbox("Sélectionner un fichier",filenames)
	        return os.path.join(folder_path,selected_filename)

    except FileNotFoundError:
    	print("Aucun chemin de fichier valide entré")

	    filename=file_selector()
	    st.info("vous avez choisi < {} >".format(filename))
	    


	    #read data↓
	    df=pd.read_csv(filename)


	#show dataset↓
	    if st.checkbox("Afficher le dataset"):
	        number=st.number_input("number of rows to view",5,10)
	        st.dataframe(df.head(number))

	    #show columns↓
	    if st.button("Afficher le nom des colonnes du dataset"):
	        st.write(df.columns)


	    #show datatypes
	    st.text("Afficher le type des colonnes du dataset ainsi que les colonnes sélectionnées↓")
	    

	    #select columns
	    all_columns=df.columns.tolist()
	    if st.checkbox("Sélectionner colonne à afficher"):
	        
	        selected_columns=st.multiselect("Veuillez sélectionner une ou plusieurs colonne",all_columns)
	        new_df=df[selected_columns]
	        st.dataframe(new_df)  
	    if st.button("Afficher le datatypes de chaque colonnes de ce data"):
	        st.write(df.dtypes)
	    if st.checkbox("Afficher le type d'élément de la colonne"):
	        nom_col=st.selectbox("choisir une colonne",all_columns)
	        col_dtype=df[nom_col].dtypes
	        st.write(col_dtype)

	    #show shape 
	    st.text("Afficher la shape du dataset, par lignes et par colonnes↓")
	    if st.checkbox("shape de dataset"):
	        st.write(df.shape)
	        data_dim=st.radio("Afficher dimension par",("Rangées","Colonnes","Rangées et Colonnes"))
	        
	        if data_dim=='Rangées':
	            st.text("Nombre de rangées")
	            st.write(df.shape[0])
	        if data_dim=='Colonnes':
	            st.text("Le nombre de colonnes")
	            st.write(df.shape[1])
	        else:
	            st.write(df.shape)

	     

	    #show values
	    all_columns=df.columns.tolist()
	    cho_col=st.selectbox("choisir une colonne",all_columns)
	    if st.button("Afficher le nombre d'éléments répétés"):
	        st.text("value counts par colonne <{}>".format(cho_col))
	        st.write(df[cho_col].value_counts())

	    
	    #show summary 
	    st.text("Afficher les statistiques descriptives du dataset↓")
	    if st.checkbox("afficher descriptives"):
	        st.write(df.describe().T)

	    ##plot and visualization
	    st.subheader("Data visualization")
	    st.text("Afficher plusieurs type de graphique dans une partie visualisation↓")
	    #correlation
	    #seaborn plot

	    if st.checkbox("correlation plot heatmap"):
	        plt.figure(figsize=(20,10))
	        st.write(sns.heatmap(df.corr(),annot=True,fmt=".2f"))
	        st.pyplot()
	    #count plot:
	    if st.checkbox("plot of value counts"):
	        st.text("value counts by target")
	        
	        primary_col=st.selectbox("primary column to groupby",all_columns)
	        selected_columns_names=st.multiselect("select columns",all_columns)
	        if st.button("plot"):
	            st.text("generate plot")
	            if selected_columns_names:
	                vc_plot=df.groupby(primary_col)[selected_columns_names].count()
	            else:
	                vc_plot=df.iloc[:,-1].value_counts()
	            st.write(vc_plot.plot(kind="bar"))
	            st.pyplot()
    except:
    	print("Veuillez sélectionner une colonne numérique, les données non numériques auront des graphiques sans signification")

	    #pie chart
	    if st.checkbox("pie plot"):
	        
	        if st.button("Generate pie plot"):
	            st.success("Generate a pie plot ")
	            st.write(df.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%%"))
	            st.pyplot()
	    


	    #customizable plot

	    st.subheader("customizable plot")
	    type_of_plot=st.selectbox("select type of plot",["area","bar","line","hist","box","kde"])
	    selected_columns_names=st.multiselect("select columns to plot",all_columns)

	    
	    if st.button("Generate plot"):
	        st.success("Generate customizable plot of {} for {}".format(type_of_plot,selected_columns_names))
	        #plot by streamlit
	        if type_of_plot=='area':
	            cust_data=df[selected_columns_names]
	            st.area_chart(cust_data) 
	        elif type_of_plot=='bar':
	            cust_data=df[selected_columns_names]
	            st.bar_chart(cust_data) 
	        elif type_of_plot=='line':
	            cust_data=df[selected_columns_names]
	            st.line_chart(cust_data) 
	        #custom plot
	        else:#elif type_of_plot=='box'
	            
	           
	            cust_plot=df[selected_columns_names].plot(kind=type_of_plot)
	            
	            st.write(cust_plot)
	            st.pyplot()
    








    if st.button("Merci"):
        st.balloons()


if __name__=='__main__':
    main()
## segmentation and klassification tif data

# packages

library(raster)
library(sf)
library(terra)
library(dplyr)
library(imageseg)
library("supercells")

# read tif data
# # shcon segmentierte Daten
seq1 <- rast("C:/Users/alexa/OneDrive/Dokumente/GitHub/Projekte/urban-green/data/segmentation-ir/649000_5479000_results.tif")
seq2 <- rast("C:/Users/alexa/OneDrive/Dokumente/GitHub/Projekte/urban-green/data/segmentation-ir/649000_5480000_results.tif")
seq3 <- rast("C:/Users/alexa/OneDrive/Dokumente/GitHub/Projekte/urban-green/data/segmentation-ir/650000_5479000_results.tif")
seq4 <- rast("C:/Users/alexa/OneDrive/Dokumente/GitHub/Projekte/urban-green/data/segmentation-ir/650000_5480000_results.tif")
seq5 <- rast("C:/Users/alexa/OneDrive/Dokumente/GitHub/Projekte/urban-green/data/segmentation-ir/651000_5479000_results.tif")
seq6 <- rast("C:/Users/alexa/OneDrive/Dokumente/GitHub/Projekte/urban-green/data/segmentation-ir/651000_5480000_results.tif")


# Orthofotos
ortho1 <- rast("C:/Users/alexa/OneDrive/Dokumente/GitHub/Projekte/urban-green/data/open-data-orthophoto/32649_5479.tif")
ortho2 <- rast("C:/Users/alexa/OneDrive/Dokumente/GitHub/Projekte/urban-green/data/open-data-orthophoto/32649_5480.tif")
ortho3 <- rast("C:/Users/alexa/OneDrive/Dokumente/GitHub/Projekte/urban-green/data/open-data-orthophoto/32650_5479.tif")
ortho4 <- rast("C:/Users/alexa/OneDrive/Dokumente/GitHub/Projekte/urban-green/data/open-data-orthophoto/32650_5480.tif")
ortho5 <- rast("C:/Users/alexa/OneDrive/Dokumente/GitHub/Projekte/urban-green/data/open-data-orthophoto/32651_5479.tif")
ortho6 <- rast("C:/Users/alexa/OneDrive/Dokumente/GitHub/Projekte/urban-green/data/open-data-orthophoto/32651_5480.tif")

#https://jakubnowosad.com/ogh2021/#31
# segmentation orthofiles

so1 <- supercells(ortho1, k = 10000, compactness = 1)
glimpse(so1)

plot(ortho1); plot(st_geometry(so1), add = TRUE, lwd = 0.5)#


vals = st_drop_geometry(so1)[c("X32649_5479_1", "X32649_5479_2", "X32649_5479_3")]
vals = vals / 255
vals = grDevices::convertColor(vals, from = "sRGB", to = "Lab")
vals

hc_vals = hclust(dist(vals), method = "ward.D2")
hc_members = cutree(hc_vals, k = 7)
plot(hc_vals, labels = row.names(hc_vals), cex = 0.5)
rect.hclust(hc_vals, k = 7, cluster = hc_members)


so1$clust = hc_members
plot(so1["clust"], main = NA)


ortho_slic_hclust = so1 %>% 
  group_by(clust) %>% 
  summarize()


#Splitting disconnected polygons:
  
  ortho_slic_hclust2 = ortho_slic_hclust %>% 
  st_geometry() %>% 
  st_collection_extract("POLYGON") %>% 
  st_cast("POLYGON", group_or_split = TRUE)

  
 # Superpixels:
    
plot(ortho1) 
plot(st_geometry(so1), 
       add = TRUE, lwd = 0.5)
  
#Clustered superpixels with dissolved borders:
    
plot(ortho1)
  plot(st_geometry(ortho_slic_hclust2),
       add = TRUE, lwd = 0.5)
  
  
plot(ortho_slic_hclust)
glimpse(ortho_slic_hclust)

ortho1_a <- st_cast(ortho_slic_hclust, "POLYGON")
plot(ortho1_a)

sf::write_sf(ortho1_a, "C:/Users/alexa/OneDrive/Dokumente/GitHub/Projekte/urban-green/R_project/output/ortho1_a.gpkg")

# SAXS Chapter

### 1 Introduction
 - As outlined in the intro SAXS is a method to get molecular envelope in solution.   
 - Radiation damage occurs with visible symptoms - changes in 1D intensity curve (aggregation would cause it to go up but we had tetrameric insulin so most of our curves go down).
 - Radiation damage caused by protein aggregation (perhaps fragmentation as well?)
 - This chapter is a study of possible mitigation in the form of scavengers.
 - Scavengers were chosen according to results in Allan *et al.* and Southworth-Davies and Garman.

### 2) RADDOSE-3D Modifications
- RADDOSE-3D was only suitable for protein crystallography. What modifications were needed so that it would work for SAXS?
- What tests were performed to make sure that the SAXS stuff worked?

### 3) Experimental Methods
- How the solutions were prepped
- Synchrotron
    - Characterisation of beam shape,
    - Photons - $500 \mu m$ diode (plots, beam picture)
- Data collection
    - Parameters
    - Table
- Dose calculation.

### 4) Analysis
- Problems faced with estimating a threshold.
- 4-Parameter logistic function along with the curvature estimate to provide a threshold value.
- Svergun method  => code written to implement the methods.

### 5) Results
- Rebecca's data
    - Results of the two metrics
        - They give very similar results
        - Only one difference
    - Most effective scavengers
- Applying Svergun method to our data
    - BsxCuBE threshold vs CorMap Threshold
    - Further analysis
    - Difference between dose and frame.
    - Most effective compounds
    - Concentration dependence
- Summary plot.

### 6) Discussion
- Now have quantitative methods.
- Releasing code!
- Current distribution of SAXS code - Eddie Snell SSRL, and Adam Round ESRF.

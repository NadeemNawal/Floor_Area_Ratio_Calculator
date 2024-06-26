def far_calc(plot_area,ratio,max_grnd_cov):
  max_covered_area= plot_area*(ratio)
  max_grnd_area= (max_grnd_cov/100)*plot_area
  print(f"The maximum covered area you can design is {max_covered_area} sq {units} with maximum ground coverage of {max_grnd_area} sq {units}.")

units=input(str("What units are you using? type 'ft' for feet and 'm' for meters: "))
plot_area= input("Enter the area of the plot: ")
plot_area= float(plot_area)
ratio=int(input("Enter the prescribed FAR 1:"))
max_grnd_cov= float(input("Enter the maximum ground coverage in percentage(%) : "))
far_calc(plot_area,ratio,max_grnd_cov)




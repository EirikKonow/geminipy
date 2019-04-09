// A object has a name "SK38", 3 x_values (123.23), same for y and z.

using System;
using System.Collections.Generic;

public class Location
{
    public string Name { get; set; }
    public List<float> Xvals { get; set; }
    public List<float> Yvals { get; set; }
    public List<float> Zvals { get; set; }
    public int Code { get; set; }
    public int Watdis { get; set; }
    public Location(string name, List<float> xvals, List<float> yvals, List<float> zvals)
    {
        Name = name;
        Xvals = xvals;
        Yvals = yvals;
        Zvals = zvals;
    }
    // Other properties, methods, events...
    public void addXval(float new_xval){
    	Xvals.Add(new_xval);
    }
}




class Program
{
    static void Main()
    {

		string name = "abc123";
		List<float> xlist = new List<float>();
		List<float> ylist = new List<float>();
		List<float> zlist = new List<float>();

		Location loc1 = new Location(name, xlist, ylist, zlist);
		loc1.addXval(123.123);

		List<float> xlistOut = loc1.Xvals;

        Console.WriteLine("loc Name = {0} Age = {1}", loc1.Name, xlistOut);

        // Keep the console open in debug mode.
        Console.WriteLine("Press any key to exit.");
        Console.ReadLine();

    }
}

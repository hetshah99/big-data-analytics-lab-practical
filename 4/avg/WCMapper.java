import java.io.IOException; 
import org.apache.hadoop.io.IntWritable; 
import org.apache.hadoop.io.LongWritable; 
import org.apache.hadoop.io.Text; 
import org.apache.hadoop.mapred.MapReduceBase; 
import org.apache.hadoop.mapred.Mapper; 
import org.apache.hadoop.mapred.OutputCollector; 
import org.apache.hadoop.mapred.Reporter; 
  
public class WCMapper extends MapReduceBase implements Mapper<LongWritable, 
                                                 Text, IntWritable, IntWritable> { 
  
    @Override
    // Map function 
    public void map(LongWritable key, Text value, OutputCollector<IntWritable,  
                                     IntWritable> output, Reporter rep) 
  
    throws IOException 
    { 
        // Splitting the line into spaces 
        String data[] = value.toString().split(" "); 
  
        for (String num : data)  
        { 
  
            int number = Integer.parseInt(num); 
  
         
                output.collect(new IntWritable(1), new IntWritable(number)); 
           
        } 
    } 
} 
import java.io.IOException; 
import org.apache.hadoop.io.IntWritable; 
import org.apache.hadoop.io.LongWritable; 
import org.apache.hadoop.io.Text; 
import org.apache.hadoop.mapred.MapReduceBase; 
import org.apache.hadoop.mapred.Mapper; 
import org.apache.hadoop.mapred.OutputCollector; 
import org.apache.hadoop.mapred.Reporter; 
  
public class WCMapper extends MapReduceBase implements Mapper<LongWritable, 
                                                Text, Text, IntWritable> { 
  
    // Map function 
    public void map(LongWritable key, Text value, OutputCollector<Text,  
                 IntWritable> output, Reporter rep) throws IOException 
    { 
  
        String line = value.toString(); 
        String[] words= line.split(" ");

        int counter= Integer.parseInt(words[0]);
        
        for(int i=1;i<=counter;i++)
        {
        	for(int j=i+1;j<=counter;j++)
        	{
        		String temp = words[i]+"." + words[j];
        		output.collect(new Text(temp), new IntWritable(1)); 
        	}
        }
    } 
} 
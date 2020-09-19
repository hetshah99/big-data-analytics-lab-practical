import java.io.IOException;
import java.util.Iterator;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.mapred.MapReduceBase;
import org.apache.hadoop.mapred.OutputCollector;
import org.apache.hadoop.mapred.Reducer;
import org.apache.hadoop.mapred.Reporter; 
  
public class WCReducer extends MapReduceBase implements Reducer<IntWritable, 
                                   IntWritable, IntWritable, IntWritable> { 
  
    @Override
    // Reduce Function 
    public void reduce(IntWritable key, Iterator<IntWritable> value, 
     OutputCollector<IntWritable, IntWritable> output, Reporter rep) 
  
    throws IOException 
    { 
  
    
    	int counter=0;
    	while (value.hasNext())  
        { 
            IntWritable i = value.next(); 
            counter++;
            if(counter==1)
            	output.collect(new IntWritable(i.get()), new IntWritable(i.get())); 
        } 
       
      
    } 
} 
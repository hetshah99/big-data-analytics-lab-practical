import java.io.IOException;
import java.util.Iterator;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.mapred.MapReduceBase;
import org.apache.hadoop.mapred.OutputCollector;
import org.apache.hadoop.mapred.Reducer;
import org.apache.hadoop.mapred.Reporter;

public class WCReducer extends MapReduceBase implements Reducer<IntWritable, IntWritable, IntWritable, IntWritable> {
  int max1 = -1000000000;
  
  public void reduce(IntWritable key, Iterator<IntWritable> value, OutputCollector<IntWritable, IntWritable> output, Reporter rep) throws IOException {
    this.max1 = Math.max(this.max1, key.get());
    output.collect(key, new IntWritable(this.max1));
  }
}

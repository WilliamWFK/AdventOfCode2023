import java.io.*;
import java.nio.file.Files;
import java.util.ArrayList;

public class Part2 {
    public static void main(String[] args) throws Exception {
        
        long lowestLocation = Long.MAX_VALUE;
        
        String content = new String(Files.readAllBytes(new File("Day5/input.txt").toPath()));

        content = content.replaceAll("[^\\\s0-9:\\n]", "");

        String[] batches = content.split(":");
        ArrayList<Map> currentMap = new ArrayList<Map>();
        ArrayList<Map> previousMap = new ArrayList<Map>();


        for(int i = batches.length-1; i >= 2; i--){
            String[] line = batches[i].split("\\n");
            for (int j = 0; j < line.length; j++){
                if (line[j].matches(".*\\d.*")){
                    String[] range = line[j].split("[\\n\s+]");
                    currentMap.add(new Map(Long.parseLong(range[0]), Long.parseLong(range[1]), Long.parseLong(range[2]), previousMap));
                }
            }
            previousMap = currentMap;
            currentMap = new ArrayList<Map>();
        }
        Map root = new Map(previousMap);

        String[] line = batches[1].strip().split("\\s+");
        for (int i = 0; i < line.length; i+=2) {
            long start = Long.parseLong(line[i]);
            long end = Long.parseLong(line[i+1]);
            for (long j = start; j <= start+end; j++){
                long location = root.findNext(j);
                if (location < lowestLocation){
                    lowestLocation = location;
                }
            }

        }
        
        System.out.println(lowestLocation);
    }
}

class Map{
    private ArrayList<Map> map;
    private long dest, source, range;

    public Map(long d, long s, long r, ArrayList<Map> m){
        dest = d;
        source = s;
        range = r-1;
        map = m;
    }

    public Map(ArrayList<Map> m){
        map = m;
    }

    public long findNext(long value){
        for(int i = 0; i < map.size(); i++){
            if(map.get(i).checkRange(value) != -1){
                return map.get(i).findNext(map.get(i).checkRange(value));
            }
        }
        if (map.size() == 0){
            return value;
        }
        else{
            return map.get(0).findNext(value);
        }
        
    }

    public long checkRange(long value){
        if(value >= source && value <= source + range){
            return dest + value - source;
        }
        return -1;
    }

    public String toString(){
        return "Dest: " + dest + " Source: " + source + " Range: " + range;
    }

}

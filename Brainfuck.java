import java.util.ArrayList;
import java.util.Queue;
import java.util.ArrayDeque;
public class Brainfuck{
  public boolean DEBUG = false;
  public String code = "";
  public Queue<Character> readQue = new ArrayDeque<Character>();
  public ArrayList<Integer> memory = new ArrayList<Integer>();
  private int memoryTarget = 0;
  private int memoryLength = 1;
  Brainfuck(){
    memory.add(0);
  }
  Brainfuck(String code){
    this();
    this.code = code;
  }
  Brainfuck(String... code){
    this();
    StringBuilder sb = new StringBuilder();
    for(String s: code) sb.append(s);
    this.code = sb.toString();
  }
	// public static void main(String[] args){
  //   String code;
  //   if(args.length == 0){
  //     System.out.println("brainfuck");
  //     return;
  //   }else{
  //     code = args[0];
  //   }
  //   System.out.println(code);
  //   Brainfuck b = new Brainfuck(code);
  //   b.run();
  //   System.out.println("");
  //   System.out.println(b.memory);
  //   System.out.println(b.memoryTarget);
	// }

  public void offerToReadQue(int i){
    readQue.offer((char)i);
  }
  public void offerToReadQue(char c){
    readQue.offer(c);
  }
  public static ArrayList<Integer> brainfuck(String code){
    Brainfuck br = new Brainfuck();
    br.run(code);
    return br.memory;
  }
  public static String brainfuckGetOutput(String code){
    Brainfuck br = new Brainfuck();
    return br.getOutput(code);
  }

  public String getOutput(){
    return getOutput(code);
  }
  public String getOutput(String code){
    // if(!output.toString().equals("")) return output.toString();
    StringBuilder output = new StringBuilder();
    int codeSize = code.length();
    int target = 0;
    while(target < codeSize){
      if(memoryTarget < 0) throw new IndexOutOfBoundsException("index: -1");
      if(DEBUG)System.out.print("before: " +code.charAt(target));
      switch(code.charAt(target)){
        case '+':
          memory.set(memoryTarget, memory.get(memoryTarget) + 1);
          break;
        case '-':
          memory.set(memoryTarget, memory.get(memoryTarget) - 1);
          break;
        case '>':
          memoryTarget++;
          if(memoryTarget >= memoryLength){
            memoryLength++;
            memory.add(0);
          }
          break;
        case '<':
          memoryTarget--;
          break;
        case '[':
          if(DEBUG)System.out.println(memory +" : "+ code);
          if(memory.get(memoryTarget) == 0){
            if(DEBUG)System.out.println("run");
            target += getCodeInSqBrackets(code, target).length();
          }else{
            if(DEBUG)System.out.println("run");
            output.append(getOutput(getCodeInSqBrackets(code, target--)));
          }
          break;
        case ']':
          break;
        case '.':
          output.append((char)(int)memory.get(memoryTarget));
          break;
        case ',':
          Character value = readQue.poll();
          if(value != null){
            memory.set(memoryTarget, (int)value);
          }else{
            try{
              memory.set(memoryTarget, System.in.read());
            }catch(java.io.IOException e){}
          }
          break;
        default:
          break;
      }
      if(DEBUG)System.out.print(" :after: ");
      if(DEBUG)System.out.println(memoryTarget+" "+code.charAt(target)+" "+memory +" "+ target);
      target++;
    }
    return output.toString();
  }
  public void run(){
    run(code);
  }
  public void run(String code){
    int codeSize = code.length();
    int target = 0;
    while(target < codeSize){
      if(memoryTarget < 0) throw new IndexOutOfBoundsException("index: -1");
      if(DEBUG)System.out.print("before: " +code.charAt(target));
      switch(code.charAt(target)){
        case '+':
          memory.set(memoryTarget, memory.get(memoryTarget) + 1);
          break;
        case '-':
          memory.set(memoryTarget, memory.get(memoryTarget) - 1);
          break;
        case '>':
          memoryTarget++;
          if(memoryTarget >= memoryLength){
            memoryLength++;
            memory.add(0);
          }
          break;
        case '<':
          memoryTarget--;
          break;
        case '[':
          if(DEBUG)System.out.println(memory +" : "+ code);
          if(memory.get(memoryTarget) == 0){
            if(DEBUG)System.out.println("run");
            target += getCodeInSqBrackets(code, target).length();
          }else{
            if(DEBUG)System.out.println("run");
            run(getCodeInSqBrackets(code, target--));
          }
          break;
        case ']':
          break;
        case '.':
          System.out.print((char)(int)memory.get(memoryTarget));
          break;
        case ',':
          Character value = readQue.poll();
          if(value != null){
            memory.set(memoryTarget, (int)value);
          }else{
            try{
              memory.set(memoryTarget, System.in.read());
            }catch(java.io.IOException e){}
          }
          break;
        default:
          break;
      }
      if(DEBUG)System.out.print(" :after: ");
      if(DEBUG)System.out.println(memoryTarget+" "+code.charAt(target)+" "+memory +" "+ target);
      target++;
    }
  }
  private String getCodeInSqBrackets(String code, int target){
    int loopCount = 1;
    StringBuilder sb = new StringBuilder();
    target++;
    findSqBrackets: while(true){
      switch(code.charAt(target)){
        case '[':
          loopCount++;
          break;
        case ']':
          loopCount--;
          if(loopCount == 0) break findSqBrackets;
          break;
        default:
          break;
      }
      sb.append(code.charAt(target++));
    }
    return sb.toString();
  }
  public Brainfuck reset(){
    memory = new ArrayList<Integer>();
    memory.add(0);
    memoryTarget = 0;
    memoryLength = 1;
    return this;
  }
  public ArrayList<Integer> getMemory(){
    return this.memory;
  }
  public int getMemoryTarget(){
    return this.memoryTarget;
  }
}

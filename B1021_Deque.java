import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class B1021_Deque {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] indexs = new int[m];
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<m; i++)
            indexs[i] = Integer.parseInt(st.nextToken());

        LinkedList<Integer> deque = new LinkedList<>();
        for(int i=1; i<n+1; i++)
            deque.offer(i);

        int count = 0;
        for(int index : indexs) {
            while(true) {
                if(deque.peek() == index) {
                    deque.poll();
                    break;
                }
                else {
                    if(deque.indexOf(index) < (double)deque.size() / 2) {
                        while(deque.peek() != index) {
                            deque.offerLast(deque.pollFirst());
                            count++;
                        }
                    }else {
                        while(deque.peek() != index) {
                            deque.offerFirst(deque.pollLast());
                            count++;
                        }
                    }
                }
            }
        }
        System.out.println(count);
    }
}
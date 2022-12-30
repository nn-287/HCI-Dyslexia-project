using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Net.Sockets;

namespace Eng.bassem_project
{
   
    public partial class Form1 : Form
    {
        TcpListener listener;
        TcpClient client;
        System.Net.Sockets.TcpClient clientSocket = new System.Net.Sockets.TcpClient();
        Timer tt = new Timer();
        Bitmap off;
        class ball
        {
            public int x, y;
            public Bitmap im;
        }
        public Form1()
        {
            this.WindowState = FormWindowState.Maximized;
            InitializeComponent();
            this.Load += Form1_Load1;
            tt.Tick += Tt_Tick;
            tt.Start();
        }

        public void Form1_Load1(object sender, EventArgs e)
        {
            off = new Bitmap(this.ClientSize.Width, this.ClientSize.Height);
            ball pnb;
            pnb = new ball();
            pnb.x = 0;
            pnb.y = 0;
            pnb.im = new Bitmap("ball.bmp");
            plist.Add(pnb);
            DrawDubb(this.CreateGraphics());
        }
        List<ball> plist = new List<ball>();
        private void Tt_Tick(object sender, EventArgs e)
        {
            NetworkStream serverStream = clientSocket.GetStream();

            byte[] bytesFrom = new byte[clientSocket.ReceiveBufferSize];
            serverStream.Read(bytesFrom, 0, (int)clientSocket.ReceiveBufferSize);

            


            string returndata = System.Text.Encoding.UTF8.GetString(bytesFrom);
            string line = returndata;
            
            string[] split = line.Split(',');

            string listtt = split[0];
            string listt2 = split[1];
            listtt = listtt.Remove(0, 1);
            string[] split2 = listt2.Split(']');
            listt2 = split2[0];

            int num1 = Int16.Parse(listtt);
            int num2 = Int16.Parse(listt2);
            plist[0].x = num1;
            plist[0].y = num2;
           // richTextBox1.Text = num1.ToString() + " , " + num2.ToString();
            DrawDubb(this.CreateGraphics());
        }
        
        private void Form1_Load(object sender, EventArgs e)
        {
            

            clientSocket.Connect("127.0.0.1", 65434);



            
                //string[] split = line.Split(',');

                //string listtt = split[0];
                //string listt2 = split[1];

                



               


                ////string[] split2 = listt2.Split(']');
                //listt2 = split2[0];

                //int num1 = Int16.Parse(listtt);
                //int num2 = Int16.Parse(listt2);

                ////int num2 = listt2 - '0';

                //MessageBox.Show(num1.ToString());
                //MessageBox.Show(num2.ToString());

            

            //byte[] bytesFrom = new byte[clientSocket.ReceiveBufferSize];
            //serverStream.Read(bytesFrom, 0, (int)clientSocket.ReceiveBufferSize);

            

            //string returndata = System.Text.Encoding.UTF8.GetString(bytesFrom);
            //string line = returndata;
            //string[] split = line.Split(',');

            //string listtt = split[0];
            //string listt2 = split[1];

            ////MessageBox.Show(returndata);

            

            //listtt = listtt.Remove(0,1);
            

            //string[] split2 = listt2.Split(']');
            //listt2 = split2[0];

            //int num1 = Int16.Parse(listtt);
            //int num2 = Int16.Parse(listt2);
            
            ////int num2 = listt2 - '0';

            //MessageBox.Show(num1.ToString()) ;
            //MessageBox.Show(num2.ToString());









        }

        void ddxrawscene(Graphics g2)
        {
            g2.Clear(Color.White);
            g2.DrawImage(plist[0].im, plist[0].x, plist[0].y);
        }
        void DrawDubb(Graphics g)
        {
            Graphics g2 = Graphics.FromImage(off);
            ddxrawscene(g2);
            g.DrawImage(off, 0, 0);
        }

        private void button1_Click(object sender, EventArgs e)
        {
           





          
        }
        public void msg(string mesg)

        {

          

        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {

        }
    }
}

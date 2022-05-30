<!--
 * @Description: 
 * @Author: hecai
 * @Date: 2022-05-09 14:57:06
 * @LastEditTime: 2022-05-30 15:56:55
 * @FilePath: \Lilygo-Wristband\README.md
-->
# Lilygo-Wristband

1. 按键程序 button.py,button1.py
   - 监控按键按下操作
   - 监控按键抬起操作
   - 通过定时器实现长按操作
   - 通过时间戳实现双击操作
  
2. 文件操作 file.py
   - 遍历删除目录,和目录下所有文件

3. 定时程序 timer.py
   - 通过延时实现定时功能
   - 通过定时器实现定时功能
   - 他们的区别在于,一个是阻塞的,一个是非阻塞的
  
4. wifi程序 wifi.py
   - wifi连接程序
  
5. 陀螺仪程序 gyroscope.py
   - 依赖:mpu9250.py,mpu6500.py,ak8963.py
   - 读取加速度信息
   - 读取角速度信息
   - 读取地磁信息
   - 读取温度信息
  
6. 心率检测程序 heart.py
   - 依赖:max39102.py,circular_buffer.py
   - 读取心率
  
7. mqtt的测试代码 mqtt.py
   - 依赖:umqttsimiple.py
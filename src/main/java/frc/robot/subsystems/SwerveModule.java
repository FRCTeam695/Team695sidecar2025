
/*
package frc.robot.subsystems;

import java.util.function.DoubleSupplier;

import com.ctre.phoenix6.hardware.CANcoder;
import com.ctre.phoenix6.hardware.TalonFX;
import edu.wpi.first.math.controller.PIDController;
import edu.wpi.first.wpilibj.smartdashboard.SmartDashboard;
import edu.wpi.first.wpilibj2.command.Command;
import edu.wpi.first.wpilibj2.command.FunctionalCommand;
import edu.wpi.first.wpilibj2.command.SubsystemBase;

public class SwerveModule {

  TalonFX driveMotor;
  TalonFX steeringMotor;
  CANcoder canCoder;
  PIDController pid;
  double angle;
  double drive;
  double L;
  double W;


  public SwerveModule (int driveMotorID, int steeringMotorID, int canID, double length, double width){
    driveMotor = new TalonFX(driveMotorID);
    steeringMotor = new TalonFX(steeringMotorID);
    canCoder = new CANcoder(canID);
    pid = new PIDController(0.0015,0,0);
    pid.enableContinuousInput(-180, 180);
    L = length;
    W = width;
  }
  

  public void driver(double[] arr){
    SmartDashboard.putNumber("PID", canCoder.getAbsolutePosition().getValueAsDouble()*360);
    angle = arr[1];
    drive = arr[0];
    if(Math.abs(canCoder.getAbsolutePosition().getValueAsDouble()*360 - arr[1]) > 90){
      if(arr[1] >= 0) angle -= 180;
      else angle += 180;
      drive *= -1;
    }
    driveMotor.set(drive);
    steeringMotor.set(pid.calculate(canCoder.getAbsolutePosition().getValueAsDouble()*360, angle));
  }
}
*/
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.EventSystems;

public class Tester : MonoBehaviour
{
    public bool mIndicator1;
    public bool mIndicator2;
    public bool mIndicator3;

    public Button mButton1;
    public Button mButton2;
    public Button mButton3;
    public Button mButton4;

    public Button mButton5;
    public Button mButton6;
    public Button mButton7;
    public Button mButton8;

    public Button mButton9;
    public Button mButton10;
    public Button mButton11;
    public Button mButton12;

    public Image mLightBulb1;
    public Image mLightBulb2;
    public Image mLightBulb3;

    public bool Button1Pressed = false;
    public bool Button2Pressed = false;
    public bool Button3Pressed = false;
    public bool Button4Pressed = false;

    public bool Button5Pressed = false;
    public bool Button6Pressed = false;
    public bool Button7Pressed = false;
    public bool Button8Pressed = false;

    public bool Button9Pressed = false;
    public bool Button10Pressed = false;
    public bool Button11Pressed = false;
    public bool Button12Pressed = false;

    public void push(int id)
    {
        #region firstifs
        if (id == 1)
        {
            Button1Pressed = !Button1Pressed;
        }

        if (id == 2)
        {
            if(Button1Pressed != true)
            {
                Button2Pressed = false;
            }
            else
            {
                Button2Pressed = true;
            }
            
        }

        if (id == 3)
        {
            if(Button2Pressed != true)
            {
                Button3Pressed = false;
            }
            else
            {
                Button3Pressed = true;
            }
        }

        if(id == 4)
        {
            if (Button3Pressed != true)
            {
                Button4Pressed = false;
            }
            else
            {
                Button4Pressed = true;
            }
        }

        #endregion

        #region secondifs
        if (id == 5)
        {
            Button5Pressed = !Button5Pressed;
        }

        if (id == 6)
        {
            if (Button5Pressed != true)
            {
                Button6Pressed = false;
            }
            else
            {
                Button6Pressed = true;
            }

        }

        if (id == 7)
        {
            if (Button6Pressed != true)
            {
                Button7Pressed = false;
            }
            else
            {
                Button7Pressed = true;
            }
        }

        if (id == 8)
        {
            if (Button7Pressed != true)
            {
                Button8Pressed = false;
            }
            else
            {
                Button8Pressed = true;
            }
        }

        #endregion

        if (id == 9)
        {
            Button9Pressed = !Button9Pressed;
        }

        if (id == 10)
        {
            if (Button9Pressed != true)
            {
                Button10Pressed = false;
            }
            else
            {
                Button10Pressed = true;
            }

        }

        if (id == 11)
        {
            if (Button10Pressed != true)
            {
                Button11Pressed = false;
            }
            else
            {
                Button11Pressed = true;
            }
        }

        if (id == 12)
        {
            if (Button11Pressed != true)
            {
                Button12Pressed = false;
            }
            else
            {
                Button12Pressed = true;
            }
        }
    }
        

    public void lightUp(int light)
    {
        if(light == 1)
        {
            if (mIndicator1 == true && Button1Pressed == true && Button2Pressed == true && Button3Pressed == true && Button4Pressed == true)
            {
                mLightBulb1.enabled = !mLightBulb1.enabled;
                if (mLightBulb1.enabled == true && mIndicator1 == true)
                {
                    Debug.Log("Win");
                }
            }
        }

        if (light == 2)
        {
            if (mIndicator2 == true && Button5Pressed == true && Button6Pressed == true && Button7Pressed == true && Button8Pressed == true)
            {
                mLightBulb2.enabled = !mLightBulb2.enabled;
                if (mLightBulb2.enabled == true && mIndicator2 == true)
                {
                    Debug.Log("Win");
                }
            }
        }

        if (light == 3)
        {
            if (mIndicator3 == true && Button9Pressed == true && Button10Pressed == true && Button11Pressed == true && Button12Pressed == true)
            {
                mLightBulb3.enabled = !mLightBulb3.enabled;
                if(mLightBulb3.enabled == true && mIndicator3 == true)
                {
                    Debug.Log("Win");
                }
            }
        }

    }



}

using System.Security.Cryptography;
using System;
using System.Security.AccessControl;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class TransitionManager {

    public string sceneName;
    public float waitTime;
    public Animator music Anim;

    void Update() {
        if(Input.GetKeyDown(KeyCode.Space)){
            StartCoroutine(ChangeScene());
        }
    }
    IEnumerator ChangeScene(){
        musicAnim.SetTrigger("fadeOut");
        yield return new WaitForSeconds(waitTime);
        SceneManager.LoadScene(sceneName);
    }
}
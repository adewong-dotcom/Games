using System.Transactions;
using System.Threading.Tasks.Dataflow;
using System.ComponentModel;
using System.Collections.ObjectModel;
using System.Collections;
using System Collections.Generic;
using UnityEngine;

public class PlayerCollision : MonoBehaviour{

    public GameObject deathEffect;

    void OnCollisionEnter(Collision col) {
        if (col.collider.tag == "Enemy")
        {
            Instantiate(deathEffect, transform.position, transform.rotation);
            GameManager.instance.EndGame();

            FindObjectOfType<AudioManager>().Play("PlayerDamage");

            Destroy(gameObject);
        }
    }
}
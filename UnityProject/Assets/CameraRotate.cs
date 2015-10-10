using UnityEngine;
using System.Collections;


public class CameraRotate : MonoBehaviour {

	static int table_number = 1;

	static void htmlMessage(int x) {
		table_number = x;

	}

	public GameObject[] targets;
	//public GameObject target = null;
	public bool rotate = false;

	float minDistance = 4f;
	// Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () 
	{

		if (targets != null) {
				transform.LookAt (targets[table_number].transform);
			if(Vector3.Distance(transform.position, targets[table_number].transform.position) > minDistance)
				transform.position = Vector3.MoveTowards(transform.position, targets[table_number].transform.position, 0.3f);
		}

		if(rotate) {
			transform.RotateAround(targets[table_number].transform.position, Vector3.up, Time.deltaTime*20);
		}
	}
}
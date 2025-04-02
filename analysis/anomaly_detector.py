from sklearn.ensemble import IsolationForest
import pandas as pd
import time

def detect_anomalies():
    while True:
        try:
            df = pd.read_csv("resource_log.txt")
            
            # 최소한 데이터가 10개 이상 모일 때까지 대기
            if len(df) >= 10:
                model = IsolationForest(contamination=0.1)
                df['Anomaly'] = model.fit_predict(df)
                df.to_csv("anomaly_log.txt", index=False)
            else:
                print("데이터가 부족합니다. 10개 이상의 데이터를 기다리는 중...")
                
        except Exception as e:
            print(f"오류 발생: {e}")
            
        time.sleep(30)

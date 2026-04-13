CREATE OR REPLACE VIEW view_temporal AS
SELECT 
    DATE_TRUNC('hour', TO_TIMESTAMP(noted_date, 'DD-MM-YYYY HH24:MI')) AS hora,
    COUNT(*) AS total_leituras
FROM temperature_readings
GROUP BY hora
ORDER BY hora;

CREATE OR REPLACE VIEW view_estatisticas AS
SELECT 
    "room_id/id" AS dispositivo,
    AVG(temp) AS media_temp,
    MAX(temp) AS max_temp,
    MIN(temp) AS min_temp
FROM temperature_readings
GROUP BY "room_id/id";

CREATE OR REPLACE VIEW view_anomalias AS
SELECT *
FROM temperature_readings
WHERE temp > 35 OR temp < 15;
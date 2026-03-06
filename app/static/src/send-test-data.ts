export {};

type SensorPayload = {
  temperature: number;
  humidity: number;
  light: number;
};

const button = document.getElementById('send-data-button');
const result = document.getElementById('result');

const randomBetween = (min: number, max: number): number => {
  return Number((Math.random() * (max - min) + min).toFixed(2));
};

const createReading = (): SensorPayload => {
  return {
    temperature: randomBetween(-10, 40),
    humidity: randomBetween(0, 100),
    light: randomBetween(0, 1000),
  };
};

const updateResultText = (text: string): void => {
  if (result) {
    result.textContent = text;
  }
};

if (button instanceof HTMLButtonElement) {
  button.addEventListener('click', async () => {
    const payload = createReading();

    try {
      const response = await fetch('/api/readings', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });

      if (!response.ok) {
        updateResultText('Failed to send reading');
        return;
      }

      updateResultText(
        `Sent temperature=${payload.temperature}, humidity=${payload.humidity}, light=${payload.light}`,
      );
    } catch {
      updateResultText('Failed to send reading');
    }
  });
}

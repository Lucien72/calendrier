from flask import Flask, request, jsonify
import calendar

Monapp = Flask(__name__)

@Monapp.route('/calendrier', methods=['GET'])
def calendrier():
    try:
        # Récupération du mois et de l'année depuis l'URL
        mois = int(request.args.get('month'))
        annee = int(request.args.get('year'))

        # Génération du calendrier selon le mois et l'année donnée
        cal = calendar.month(annee, mois)

        return jsonify({"calendar": cal}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    Monapp.run()

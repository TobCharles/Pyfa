from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.hull = "Loki"
        self.sub = "Loki Defensive - Warfare Processor"
        self.skill = "Minmatar Defensive Systems"

    # Subsystem Skill Bonus:
    # 5% bonus to effectiveness of Skirmish Warfare Links per subsystem skill level

    def test_minmatarDefensiveSystems_commandBonus_moduleGangCoordinatorSkillrqSkirmishWarfare(self):
        self.buildTested = 0
        attr = "commandBonus"
        item = "Skirmish Warfare Link - Interdiction Maneuvers I"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl), ship=self.hull, miscitms=self.sub)
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl), ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_minmatarDefensiveSystems_commandBonus_moduleGangCoordinatorSkillrqOther(self):
        self.buildTested = 0
        attr = "commandBonus"
        item = "Information Warfare Link - Recon Operation I"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl), ship=self.hull, miscitms=self.sub)
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl), ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Role Bonus:
    # 99% reduction in Warfare Link module CPU need

    def test_static_cpu_moduleGangCoordinatorSkillrqLeadership(self):
        self.buildTested = 0
        attr = "cpu"
        item = "Siege Warfare Link - Active Shielding I"
        iIngame = 1.0
        fIngame = 0.01
        iEos = self.getItemAttr(attr, item, ship=self.hull)
        fEos = self.getItemAttr(attr, item, ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_static_cpu_moduleGangCoordinatorNoSkillrqLeadership(self):
        self.buildTested = 0
        attr = "cpu"
        item = "Command Processor I"
        iIngame = 1.0
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, ship=self.hull)
        fEos = self.getItemAttr(attr, item, ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Hidden bonus:
    # Add slots to ship

    def test_static_hiSlots_ship(self):
        self.buildTested = 0
        attr = "hiSlots"
        iIngame = 0.0
        fIngame = 1.0
        iEos = self.getShipAttr(attr, ship=self.hull) or 0.0
        fEos = self.getShipAttr(attr, ship=self.hull, miscitms=self.sub) or 0.0
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_static_medSlots_ship(self):
        self.buildTested = 0
        attr = "medSlots"
        iIngame = 0.0
        fIngame = 1.0
        iEos = self.getShipAttr(attr, ship=self.hull) or 0.0
        fEos = self.getShipAttr(attr, ship=self.hull, miscitms=self.sub) or 0.0
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_static_lowSlots_ship(self):
        self.buildTested = 0
        attr = "lowSlots"
        iIngame = 0.0
        fIngame = 0.0
        iEos = self.getShipAttr(attr, ship=self.hull) or 0.0
        fEos = self.getShipAttr(attr, ship=self.hull, miscitms=self.sub) or 0.0
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Hidden bonus:
    # +1400000 kg mass

    def test_static_mass_ship(self):
        self.buildTested = 0
        attr = "mass"
        iIngame = 6540000.0
        fIngame = 7940000.0
        iEos = self.getShipAttr(attr, ship=self.hull)
        fEos = self.getShipAttr(attr, ship=self.hull, miscitms=self.sub)
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Hidden bonus:
    # 130 m signature radius

    def test_static_signatureRadius_ship(self):
        self.buildTested = 0
        attr = "signatureRadius"
        ingame = 130.0
        eos = self.getShipAttr(attr, ship=self.hull, miscitms=self.sub)
        self.assertAlmostEquals(eos, ingame)

    # Hidden bonus:
    # 200 m3 cargohold capacity

    def test_static_capacity_ship(self):
        self.buildTested = 0
        attr = "capacity"
        ingame = 200.0
        eos = self.getShipAttr(attr, ship=self.hull, miscitms=self.sub)
        self.assertAlmostEquals(eos, ingame)

    # Hidden bonus:
    # Assign ship armor resistances

    def test_static_armorEmDamageResonance_ship(self):
        self.buildTested = 0
        attr = "armorEmDamageResonance"
        ingame = 0.1
        eos = self.getShipAttr(attr, ship=self.hull, miscitms=self.sub)
        self.assertAlmostEquals(eos, ingame)

    def test_static_armorExplosiveDamageResonance_ship(self):
        self.buildTested = 0
        attr = "armorExplosiveDamageResonance"
        ingame = 0.9
        eos = self.getShipAttr(attr, ship=self.hull, miscitms=self.sub)
        self.assertAlmostEquals(eos, ingame)

    def test_static_armorKineticDamageResonance_ship(self):
        self.buildTested = 0
        attr = "armorKineticDamageResonance"
        ingame = 0.75
        eos = self.getShipAttr(attr, ship=self.hull, miscitms=self.sub)
        self.assertAlmostEquals(eos, ingame)

    def test_static_armorThermalDamageResonance_ship(self):
        self.buildTested = 0
        attr = "armorThermalDamageResonance"
        ingame = 0.325
        eos = self.getShipAttr(attr, ship=self.hull, miscitms=self.sub)
        self.assertAlmostEquals(eos, ingame)

    # Hidden bonus:
    # Assign ship shield resistances

    def test_static_shieldEmDamageResonance_ship(self):
        self.buildTested = 0
        attr = "shieldEmDamageResonance"
        ingame = 0.25
        eos = self.getShipAttr(attr, ship=self.hull, miscitms=self.sub)
        self.assertAlmostEquals(eos, ingame)

    def test_static_shieldExplosiveDamageResonance_ship(self):
        self.buildTested = 0
        attr = "shieldExplosiveDamageResonance"
        ingame = 0.5
        eos = self.getShipAttr(attr, ship=self.hull, miscitms=self.sub)
        self.assertAlmostEquals(eos, ingame)

    def test_static_shieldKineticDamageResonance_ship(self):
        self.buildTested = 0
        attr = "shieldKineticDamageResonance"
        ingame = 0.6
        eos = self.getShipAttr(attr, ship=self.hull, miscitms=self.sub)
        self.assertAlmostEquals(eos, ingame)

    def test_static_shieldThermalDamageResonance_ship(self):
        self.buildTested = 0
        attr = "shieldThermalDamageResonance"
        ingame = 0.4
        eos = self.getShipAttr(attr, ship=self.hull, miscitms=self.sub)
        self.assertAlmostEquals(eos, ingame)

    # Hidden bonus:
    # +2050 armor hp

    def test_static_armorHP_ship(self):
        self.buildTested = 0
        attr = "armorHP"
        iIngame = 100.0
        fIngame = 2150.0
        iEos = self.getShipAttr(attr, ship=self.hull)
        fEos = self.getShipAttr(attr, ship=self.hull, miscitms=self.sub)
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Hidden bonus:
    # +3100 shield capacity

    def test_static_shieldCapacity_ship(self):
        self.buildTested = 0
        attr = "shieldCapacity"
        iIngame = 100.0
        fIngame = 3200.0
        iEos = self.getShipAttr(attr, ship=self.hull)
        fEos = self.getShipAttr(attr, ship=self.hull, miscitms=self.sub)
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Hidden bonus:
    # +1620 seconds shield recharge rate

    def test_static_shieldRechargeRate_ship(self):
        self.buildTested = 0
        attr = "shieldRechargeRate"
        iIngame = 10000.0
        fIngame = 1630000.0
        iEos = self.getShipAttr(attr, ship=self.hull)
        fEos = self.getShipAttr(attr, ship=self.hull, miscitms=self.sub)
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)
# DB2ADMIN.LCNELEMENTS

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 105
- **Primary key**: `COMPANYCODE`, `ITEMTYPECODE`, `SUBCODEKEY`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 47282

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SUBCODEKEY` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 3 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `RECORDNUMBER` | CHAR(10) |  |  |  |  |
| 5 | `DATETESTED` | DATE |  |  |  |  |
| 6 | `PROJECTILE` | CHAR(30) |  |  |  |  |
| 7 | `WEIGHT` | CHAR(30) |  |  |  |  |
| 8 | `CASE` | CHAR(30) |  |  |  |  |
| 9 | `POWDER` | CHAR(30) |  |  |  |  |
| 10 | `BARRELLENGTH` | CHAR(30) |  |  |  |  |
| 11 | `OBLIQUITY` | CHAR(30) |  |  |  |  |
| 12 | `TESTSPEC` | CHAR(30) |  |  |  |  |
| 13 | `TEMPERATURE` | CHAR(10) |  |  |  |  |
| 14 | `HUMIDITY` | CHAR(10) |  |  |  |  |
| 15 | `CLAYCALIBRATION` | CHAR(10) |  |  |  |  |
| 16 | `MUZZLETARGET` | CHAR(10) |  |  |  |  |
| 17 | `MUZZLESCREENONE` | CHAR(10) |  |  |  |  |
| 18 | `SCREENONETHREE` | CHAR(10) |  |  |  |  |
| 19 | `SCREENTHREETARGET` | CHAR(10) |  |  |  |  |
| 20 | `MIDPOINTTARGET` | CHAR(10) |  |  |  |  |
| 21 | `TARGETWITNESS` | CHAR(10) |  |  |  |  |
| 22 | `WITNESSPANEL` | CHAR(10) |  |  |  |  |
| 23 | `SHOTONE` | CHAR(5) |  |  |  |  |
| 24 | `SHOTTWO` | CHAR(5) |  |  |  |  |
| 25 | `SHOTTHREE` | CHAR(5) |  |  |  |  |
| 26 | `SHOTFOUR` | CHAR(5) |  |  |  |  |
| 27 | `SHOTFIVE` | CHAR(5) |  |  |  |  |
| 28 | `SHOTSIX` | CHAR(5) |  |  |  |  |
| 29 | `SHOTSEVEN` | CHAR(5) |  |  |  |  |
| 30 | `SHOTEIGHT` | CHAR(5) |  |  |  |  |
| 31 | `FIRSTCHRONOGRAPHONE` | CHAR(5) |  |  |  |  |
| 32 | `FIRSTCHRONOGRAPHTWO` | CHAR(5) |  |  |  |  |
| 33 | `FIRSTCHRONOGRAPHTHREE` | CHAR(5) |  |  |  |  |
| 34 | `FIRSTCHRONOGRAPHFOUR` | CHAR(5) |  |  |  |  |
| 35 | `FIRSTCHRONOGRAPHFIVE` | CHAR(5) |  |  |  |  |
| 36 | `FIRSTCHRONOGRAPHSIX` | CHAR(5) |  |  |  |  |
| 37 | `FIRSTCHRONOGRAPHSEVEN` | CHAR(5) |  |  |  |  |
| 38 | `FIRSTCHRONOGRAPHEIGHT` | CHAR(5) |  |  |  |  |
| 39 | `FIRSTVELOCITYONE` | CHAR(5) |  |  |  |  |
| 40 | `FIRSTVELOCITYTWO` | CHAR(5) |  |  |  |  |
| 41 | `FIRSTVELOCITYTHREE` | CHAR(5) |  |  |  |  |
| 42 | `FIRSTVELOCITYFOUR` | CHAR(5) |  |  |  |  |
| 43 | `FIRSTVELOCITYFIVE` | CHAR(5) |  |  |  |  |
| 44 | `FIRSTVELOCITYSIX` | CHAR(5) |  |  |  |  |
| 45 | `FIRSTVELOCITYSEVEN` | CHAR(5) |  |  |  |  |
| 46 | `FIRSTVELOCITYEIGHT` | CHAR(5) |  |  |  |  |
| 47 | `SECONDCHRONOGRAPHONE` | CHAR(5) |  |  |  |  |
| 48 | `SECONDCHRONOGRAPHTWO` | CHAR(5) |  |  |  |  |
| 49 | `SECONDCHRONOGRAPHTHREE` | CHAR(5) |  |  |  |  |
| 50 | `SECONDCHRONOGRAPHFOUR` | CHAR(5) |  |  |  |  |
| 51 | `SECONDCHRONOGRAPHFIVE` | CHAR(5) |  |  |  |  |
| 52 | `SECONDCHRONOGRAPHSIX` | CHAR(5) |  |  |  |  |
| 53 | `SECONDCHRONOGRAPHSEVEN` | CHAR(5) |  |  |  |  |
| 54 | `SECONDCHRONOGRAPHEIGHT` | CHAR(5) |  |  |  |  |
| 55 | `SECONDVELOCITYONE` | CHAR(5) |  |  |  |  |
| 56 | `SECONDVELOCITYTWO` | CHAR(5) |  |  |  |  |
| 57 | `SECONDVELOCITYTHREE` | CHAR(5) |  |  |  |  |
| 58 | `SECONDVELOCITYFOUR` | CHAR(5) |  |  |  |  |
| 59 | `SECONDVELOCITYFIVE` | CHAR(5) |  |  |  |  |
| 60 | `SECONDVELOCITYSIX` | CHAR(5) |  |  |  |  |
| 61 | `SECONDVELOCITYSEVEN` | CHAR(5) |  |  |  |  |
| 62 | `SECONDVELOCITYEIGHT` | CHAR(5) |  |  |  |  |
| 63 | `AVEVELOCITYONE` | CHAR(5) |  |  |  |  |
| 64 | `AVEVELOCITYTWO` | CHAR(5) |  |  |  |  |
| 65 | `AVEVELOCITYTHREE` | CHAR(5) |  |  |  |  |
| 66 | `AVEVELOCITYFOUR` | CHAR(5) |  |  |  |  |
| 67 | `AVEVELOCITYFIVE` | CHAR(5) |  |  |  |  |
| 68 | `AVEVELOCITYSIX` | CHAR(5) |  |  |  |  |
| 69 | `AVEVELOCITYSEVEN` | CHAR(5) |  |  |  |  |
| 70 | `AVEVELOCITYEIGHT` | CHAR(5) |  |  |  |  |
| 71 | `CORRAVEVELOCITYONE` | CHAR(5) |  |  |  |  |
| 72 | `CORRAVEVELOCITYTWO` | CHAR(5) |  |  |  |  |
| 73 | `CORRAVEVELOCITYTHREE` | CHAR(5) |  |  |  |  |
| 74 | `CORRAVEVELOCITYFOUR` | CHAR(5) |  |  |  |  |
| 75 | `CORRAVEVELOCITYFIVE` | CHAR(5) |  |  |  |  |
| 76 | `CORRAVEVELOCITYSIX` | CHAR(5) |  |  |  |  |
| 77 | `CORRAVEVELOCITYSEVEN` | CHAR(5) |  |  |  |  |
| 78 | `CORRAVEVELOCITYEIGHT` | CHAR(5) |  |  |  |  |
| 79 | `LOSSONE` | CHAR(5) |  |  |  |  |
| 80 | `LOSSTWO` | CHAR(5) |  |  |  |  |
| 81 | `LOSSTHREE` | CHAR(5) |  |  |  |  |
| 82 | `LOSSFOUR` | CHAR(5) |  |  |  |  |
| 83 | `LOSSFIVE` | CHAR(5) |  |  |  |  |
| 84 | `LOSSSIX` | CHAR(5) |  |  |  |  |
| 85 | `LOSSSEVEN` | CHAR(5) |  |  |  |  |
| 86 | `LOSSEIGHT` | CHAR(5) |  |  |  |  |
| 87 | `SHOTINCLUDEDONE` | CHAR(5) |  |  |  |  |
| 88 | `SHOTINCLUDEDTWO` | CHAR(5) |  |  |  |  |
| 89 | `SHOTINCLUDEDTHREE` | CHAR(5) |  |  |  |  |
| 90 | `SHOTINCLUDEDFOUR` | CHAR(5) |  |  |  |  |
| 91 | `SHOTINCLUDEDFIVE` | CHAR(5) |  |  |  |  |
| 92 | `SHOTINCLUDEDSIX` | CHAR(5) |  |  |  |  |
| 93 | `SHOTINCLUDEDSEVEN` | CHAR(5) |  |  |  |  |
| 94 | `SHOTINCLUDEDEIGHT` | CHAR(5) |  |  |  |  |
| 95 | `PENETRATIONONE` | CHAR(5) |  |  |  |  |
| 96 | `PENETRATIONTWO` | CHAR(5) |  |  |  |  |
| 97 | `PENETRATIONTHREE` | CHAR(5) |  |  |  |  |
| 98 | `PENETRATIONFOUR` | CHAR(5) |  |  |  |  |
| 99 | `PENETRATIONFIVE` | CHAR(5) |  |  |  |  |
| 100 | `PENETRATIONSIX` | CHAR(5) |  |  |  |  |
| 101 | `PENETRATIONSEVEN` | CHAR(5) |  |  |  |  |
| 102 | `PENETRATIONEIGHT` | CHAR(5) |  |  |  |  |
| 103 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 104 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `LCNELEMENTS.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LCNELEMENTS.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND LCNELEMENTS.ITEMTYPECODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LCNELEMENTSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODEKEY,
       t.CODE,
       t.RECORDNUMBER,
       t.DATETESTED,
       t.PROJECTILE,
       t.WEIGHT,
       t.CASE,
       t.POWDER,
       t.BARRELLENGTH,
       t.OBLIQUITY
FROM   DB2ADMIN.LCNELEMENTS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

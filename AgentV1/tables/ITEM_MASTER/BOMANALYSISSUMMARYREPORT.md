# DB2ADMIN.BOMANALYSISSUMMARYREPORT

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'BOM')
- **Roles**: `business_data`
- **Columns**: 49
- **Primary key**: `IDENTIFIER`, `PROGRESSIVE`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 1550

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IDENTIFIER` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `PROGRESSIVE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `COMPANYCODE` | CHAR(3) |  | FK | foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `NUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 4 | `ITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 6 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 7 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 8 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUFFIXCODE` | CHAR(20) |  |  |  |  |
| 16 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 17 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 18 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 19 | `BOMSUBCODE01` | CHAR(20) |  |  |  |  |
| 20 | `BOMSUBCODE02` | CHAR(10) |  |  |  |  |
| 21 | `BOMSUBCODE03` | CHAR(10) |  |  |  |  |
| 22 | `BOMSUBCODE04` | CHAR(10) |  |  |  |  |
| 23 | `BOMSUBCODE05` | CHAR(10) |  |  |  |  |
| 24 | `BOMSUBCODE06` | CHAR(10) |  |  |  |  |
| 25 | `BOMSUBCODE07` | CHAR(10) |  |  |  |  |
| 26 | `BOMSUBCODE08` | CHAR(10) |  |  |  |  |
| 27 | `BOMSUBCODE09` | CHAR(10) |  |  |  |  |
| 28 | `BOMSUBCODE10` | CHAR(10) |  |  |  |  |
| 29 | `REFBOMSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 30 | `TECHNICALBOMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 31 | `PRODUCTIONBOMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 32 | `COSTCALCULATIONBOMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 33 | `GENERICREFERENCE` | CHAR(20) |  |  |  |  |
| 34 | `PLANTCODE` | CHAR(8) |  | FK | foreign_key |  |
| 35 | `COSTGROUPCODE` | CHAR(3) |  | FK | foreign_key |  |
| 36 | `BOMUOMTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 37 | `BOMUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 38 | `BOMQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 39 | `QUANTITYPERTYPE` | CHAR(2) |  |  |  |  |
| 40 | `BOMINCIDENCE` | DECIMAL(5,2) |  |  |  |  |
| 41 | `STATUS` | CHAR(1) |  |  |  |  |
| 42 | `APPROVALDATE` | DATE |  |  |  |  |
| 43 | `APPROVALUSER` | CHAR(50) |  |  |  |  |
| 44 | `RELEASEDATE` | DATE |  |  |  |  |
| 45 | `RELEASEUSER` | CHAR(50) |  |  |  |  |
| 46 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 47 | `PLANTCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 48 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `BOMANALYSISSUMMARYREPORT.COMPANYCODE = COMPANY.CODE` |
| `COSTGROUP_COSTGROUP` | `COMPANYCODE`, `COSTGROUPCODE` | [`COSTGROUP`](../COSTING/COSTGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BOMANALYSISSUMMARYREPORT.COMPANYCODE = COSTGROUP.COMPANYCODE AND BOMANALYSISSUMMARYREPORT.COSTGROUPCODE = COSTGROUP.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BOMANALYSISSUMMARYREPORT.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND BOMANALYSISSUMMARYREPORT.ITEMTYPECODE = ITEMTYPE.CODE` |
| `PLANT_PLANT` | `PLANTCOMPANYCODE`, `PLANTCODE` | [`PLANT`](../CORE_MASTER/PLANT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BOMANALYSISSUMMARYREPORT.PLANTCOMPANYCODE = PLANT.COMPANYCODE AND BOMANALYSISSUMMARYREPORT.PLANTCODE = PLANT.CODE` |
| `UNITOFMEASURE_BOMUOM` | `BOMUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `BOMANALYSISSUMMARYREPORT.BOMUOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `BOMANALYSISSUMMARYREPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.IDENTIFIER,
       t.PROGRESSIVE,
       t.COMPANYCODE,
       t.NUMBERID,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07
FROM   DB2ADMIN.BOMANALYSISSUMMARYREPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

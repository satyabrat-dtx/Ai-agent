# DB2ADMIN.DESIGN

- **Module**: `PRODUCTION` (low confidence — FK neighbourhood: 1 of 1 related tables are PRODUCTION)
- **Roles**: `business_data`
- **Columns**: 53
- **Primary key**: `COMPANYCODE`, `NUMBERID`
- **FK degree**: referenced by 2 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 37535

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `NUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 4 | `ITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `DESIGNTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 6 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 7 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 8 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUFFIXCODE` | CHAR(20) |  |  |  |  |
| 17 | `GENERICDESIGN` | SMALLINT | NOT NULL |  |  |  |
| 18 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 19 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 20 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 21 | `IMAGENAME` | CHAR(80) |  |  |  |  |
| 22 | `IMAGEPATH` | CHAR(30) |  |  |  |  |
| 23 | `GENERICREFERENCE` | CHAR(20) |  |  |  |  |
| 24 | `VALIDFROMDATE` | DATE |  |  |  |  |
| 25 | `VALIDTODATE` | DATE |  |  |  |  |
| 26 | `STANDARDBATCHSIZE` | DECIMAL(15,5) |  |  |  |  |
| 27 | `STANDARDBATCHSIZEUMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 28 | `NUMBEROFSCREENS` | INTEGER | NOT NULL |  |  |  |
| 29 | `HANDLESCREENS` | CHAR(2) |  |  |  |  |
| 30 | `RESERVATIONWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 31 | `PRODUCTIONRESERVATIONGROUPCODE` | CHAR(3) |  | FK | foreign_key |  |
| 32 | `AVERAGESCREENLIFEINUM` | INTEGER | NOT NULL |  |  |  |
| 33 | `AVERAGESCREENLIFEINMONTH` | INTEGER | NOT NULL |  |  |  |
| 34 | `COSTELMFORSCREENITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 35 | `COSTELEMENTFORSCREENSUBCODE01` | CHAR(20) |  |  |  |  |
| 36 | `COSTELMFORINTRESTITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 37 | `COSTELEMENTFORINTRESTSUBCODE01` | CHAR(20) |  |  |  |  |
| 38 | `SCREENSTANDARDCOST` | DECIMAL(18,5) |  |  |  |  |
| 39 | `STATUS` | CHAR(1) | NOT NULL |  |  |  |
| 40 | `APPROVALDATE` | DATE |  |  |  |  |
| 41 | `APPROVALUSER` | CHAR(50) |  |  |  |  |
| 42 | `RELEASEDATE` | DATE |  |  |  |  |
| 43 | `RELEASEUSER` | CHAR(50) |  |  |  |  |
| 44 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 45 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 46 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 47 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 48 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 49 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 50 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 51 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 52 | `ARTICLESTATUSCODE` | CHAR(8) |  | FK | foreign_key |  |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ARTICLESTATUS_ARTICLESTATUS` | `COMPANYCODE`, `ITEMTYPECODE`, `ARTICLESTATUSCODE` | [`ARTICLESTATUS`](../OTHER/ARTICLESTATUS.md) | `COMPANYCODE`, `ITEMTYPECODE`, `CODE` | RESTRICT | `DESIGN.COMPANYCODE = ARTICLESTATUS.COMPANYCODE AND DESIGN.ITEMTYPECODE = ARTICLESTATUS.ITEMTYPECODE AND DESIGN.ARTICLESTATUSCODE = ARTICLESTATUS.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `DESIGN.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `DESIGN.COMPANYCODE = DIVISION.COMPANYCODE AND DESIGN.DIVISIONCODE = DIVISION.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `DESIGN.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND DESIGN.ITEMTYPECODE = ITEMTYPE.CODE` |
| `PRODUCTIONRESERVATIONGROUP_PRODUCTIONRESERVATIONGROUP` | `COMPANYCODE`, `PRODUCTIONRESERVATIONGROUPCODE` | [`PRODUCTIONRESERVATIONGROUP`](../PRODUCTION/PRODUCTIONRESERVATIONGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `DESIGN.COMPANYCODE = PRODUCTIONRESERVATIONGROUP.COMPANYCODE AND DESIGN.PRODUCTIONRESERVATIONGROUPCODE = PRODUCTIONRESERVATIONGROUP.CODE` |
| `UNITOFMEASURE_STANDARDBATCHSIZEUM` | `STANDARDBATCHSIZEUMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `DESIGN.STANDARDBATCHSIZEUMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `DESIGN_ENGINEERINGCHANGELOG` | [`DESIGNENGINEERINGCHANGELOG`](../LOGISTICS/DESIGNENGINEERINGCHANGELOG.md) | `DESIGNCOMPANYCODE`, `DESIGNNUMBERID` | `DESIGNENGINEERINGCHANGELOG.DESIGNCOMPANYCODE = DESIGN.COMPANYCODE AND DESIGNENGINEERINGCHANGELOG.DESIGNNUMBERID = DESIGN.NUMBERID` |
| `DESIGN_DESIGNCOMPONENT` | [`DESIGNCOMPONENT`](../PRODUCTION/DESIGNCOMPONENT.md) | `DESIGNCOMPANYCODE`, `DESIGNNUMBERID` | `DESIGNCOMPONENT.DESIGNCOMPANYCODE = DESIGN.COMPANYCODE AND DESIGNCOMPONENT.DESIGNNUMBERID = DESIGN.NUMBERID` |

## Implicit links (NOT declared in the DDL — inferred)

- child `DESIGNCOMPONENTBEAN`.`FATHERID` → this table's `ABSUNIQUEID` (medium confidence)

## Indexes

- `DESIGNUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.NUMBERID,
       t.ITEMTYPECODE,
       t.DESIGNTEMPLATECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06
FROM   DB2ADMIN.DESIGN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

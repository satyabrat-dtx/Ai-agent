# DB2ADMIN.GARMENTORDERPACKINGGROUP

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 52
- **Primary key**: `COMPANYCODE`, `SALORDLINESALORDERCOUNTERCODE`, `SALESORDERLINESALESORDERCODE`, `SALESORDERLINEORDERLINE`, `SALESORDERLINEORDERSUBLINE`, `SALORDLINECOMPONENTORDERLINE`, `PACKINGGROUP`
- **FK degree**: referenced by 0 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 197115

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `SALORDLINESALORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SALESORDERLINESALESORDERCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `SALESORDERLINEORDERLINE` | DECIMAL(7,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `SALESORDERLINEORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `SALORDLINECOMPONENTORDERLINE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `PACKINGGROUP` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 7 | `PACKINGGROUPDESCRIPTION` | CHAR(200) |  |  |  |  |
| 8 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 9 | `ITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 10 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 11 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `QUANTITYTYPE` | CHAR(1) |  |  |  |  |
| 21 | `COLORCODE` | CHAR(10) |  |  |  |  |
| 22 | `SIZECODE` | CHAR(10) |  |  |  |  |
| 23 | `PACKINGTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 24 | `PACKINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 25 | `TOTALCARTONS` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 26 | `WEIGHTUNITOFMEASURECODE` | CHAR(3) |  | FK | foreign_key |  |
| 27 | `WEIGHTNET` | DECIMAL(15,5) |  |  |  |  |
| 28 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 29 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 30 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 31 | `LENGTH` | DECIMAL(7,2) |  |  |  |  |
| 32 | `WIDTH` | DECIMAL(7,2) |  |  |  |  |
| 33 | `HEIGHT` | DECIMAL(7,2) |  |  |  |  |
| 34 | `DIMENSIONUNITOFMEASURECODE` | CHAR(3) |  | FK | foreign_key |  |
| 35 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 36 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 37 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 38 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 39 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 40 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 41 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 42 | `CANCELLEDCARTONS` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 43 | `WEIGHTREALNET` | DECIMAL(15,5) |  |  |  |  |
| 44 | `VOLUMEUNITOFMEASURECODE` | CHAR(3) |  | FK | foreign_key |  |
| 45 | `VOLUMECONVERSIONRATE` | DECIMAL(15,5) |  |  |  |  |
| 46 | `APPROVALLEVEL` | CHAR(2) |  |  |  |  |
| 47 | `FIRSTLEVELAPPROVALDATE` | DATE |  |  |  |  |
| 48 | `FIRSTLEVELAPPROVALUSER` | CHAR(50) |  |  |  |  |
| 49 | `SECONDLEVELAPPROVALDATE` | DATE |  |  |  |  |
| 50 | `SECONDLEVELAPPROVALUSER` | CHAR(50) |  |  |  |  |
| 51 | `LINKEDSIZECODE` | CHAR(10) |  |  |  |  |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `GARMENTORDERPACKINGGROUP.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `GARMENTORDERPACKINGGROUP.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND GARMENTORDERPACKINGGROUP.ITEMTYPECODE = ITEMTYPE.CODE` |
| `SALESORDERLINE_SALESORDERLINE` | `COMPANYCODE`, `SALORDLINESALORDERCOUNTERCODE`, `SALESORDERLINESALESORDERCODE`, `SALESORDERLINEORDERLINE`, `SALESORDERLINEORDERSUBLINE`, `SALORDLINECOMPONENTORDERLINE` | [`SALESORDERLINE`](../SALES/SALESORDERLINE.md) | `SALESORDERCOMPANYCODE`, `SALESORDERCOUNTERCODE`, `SALESORDERCODE`, `ORDERLINE`, `ORDERSUBLINE`, `COMPONENTORDERLINE` | RESTRICT | `GARMENTORDERPACKINGGROUP.COMPANYCODE = SALESORDERLINE.SALESORDERCOMPANYCODE AND GARMENTORDERPACKINGGROUP.SALORDLINESALORDERCOUNTERCODE = SALESORDERLINE.SALESORDERCOUNTERCODE AND GARMENTORDERPACKINGGROUP.SALESORDERLINESALESORDERCODE = SALESORDERLINE.SALESORDERCODE AND GARMENTORDERPACKINGGROUP.SALESORDERLINEORDERLINE = SALESORDERLINE.ORDERLINE AND GARMENTORDERPACKINGGROUP.SALESORDERLINEORDERSUBLINE = SALESORDERLINE.ORDERSUBLINE AND GARMENTORDERPACKINGGROUP.SALORDLINECOMPONENTORDERLINE = SALESORDERLINE.COMPONENTORDERLINE` |
| `UNITOFMEASURE_DIMENSIONUNITOFMEASURE` | `DIMENSIONUNITOFMEASURECODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `GARMENTORDERPACKINGGROUP.DIMENSIONUNITOFMEASURECODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_VOLUMEUNITOFMEASURE` | `VOLUMEUNITOFMEASURECODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `GARMENTORDERPACKINGGROUP.VOLUMEUNITOFMEASURECODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_WEIGHTUNITOFMEASURE` | `WEIGHTUNITOFMEASURECODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `GARMENTORDERPACKINGGROUP.WEIGHTUNITOFMEASURECODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `GARMENTORDERPACKINGGROUPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.SALORDLINESALORDERCOUNTERCODE,
       t.SALESORDERLINESALESORDERCODE,
       t.SALESORDERLINEORDERLINE,
       t.SALESORDERLINEORDERSUBLINE,
       t.SALORDLINECOMPONENTORDERLINE,
       t.PACKINGGROUP,
       t.PACKINGGROUPDESCRIPTION,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02
FROM   DB2ADMIN.GARMENTORDERPACKINGGROUP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

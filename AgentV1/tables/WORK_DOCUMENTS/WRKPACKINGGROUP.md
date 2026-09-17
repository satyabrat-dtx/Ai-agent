# DB2ADMIN.WRKPACKINGGROUP

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 49
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 197453

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CHOOSE` | SMALLINT | NOT NULL |  |  |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `SALORDLINESALORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 4 | `SALESORDERLINESALESORDERCODE` | CHAR(15) |  |  |  |  |
| 5 | `SALESORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 6 | `SALESORDERLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 7 | `SALORDLINECOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 8 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 9 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 10 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 11 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 12 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 13 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `PRODUCTCODE` | CHAR(120) |  |  |  |  |
| 23 | `COLORCODE` | CHAR(10) |  |  |  |  |
| 24 | `SIZECODE` | CHAR(10) |  |  |  |  |
| 25 | `PACKINGGROUP` | CHAR(15) |  |  |  |  |
| 26 | `PACKINGGROUPDESCRIPTION` | CHAR(200) |  |  |  |  |
| 27 | `PACKINGTYPE` | CHAR(1) |  |  |  |  |
| 28 | `SOLINEQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 29 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 30 | `TOTALCARTONS` | DECIMAL(11,0) |  |  |  |  |
| 31 | `TOTALPOSSIBLECARTONS` | DECIMAL(11,0) |  |  |  |  |
| 32 | `LEFTOVERQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 33 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 34 | `WEIGHTNET` | DECIMAL(15,5) |  |  |  |  |
| 35 | `WEIGHTUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 36 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 37 | `LENGTH` | DECIMAL(7,2) |  |  |  |  |
| 38 | `WIDTH` | DECIMAL(7,2) |  |  |  |  |
| 39 | `HEIGHT` | DECIMAL(7,2) |  |  |  |  |
| 40 | `DIMENSIONUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 41 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 42 | `ROWIDENTIFIER` | INTEGER | NOT NULL |  |  |  |
| 43 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 44 | `TOLERANCEQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 45 | `WEIGHTREALNET` | DECIMAL(15,5) |  |  |  |  |
| 46 | `VOLUMEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 47 | `VOLUMECONVERSIONRATE` | DECIMAL(15,5) |  |  |  |  |
| 48 | `LINKEDSIZECODE` | CHAR(10) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKPACKINGGROUPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CHOOSE,
       t.COMPANYCODE,
       t.SALORDLINESALORDERCOUNTERCODE,
       t.SALESORDERLINESALESORDERCODE,
       t.SALESORDERLINEORDERLINE,
       t.SALESORDERLINEORDERSUBLINE,
       t.SALORDLINECOMPONENTORDERLINE,
       t.EXTERNALREFERENCE,
       t.LINENO,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE
FROM   DB2ADMIN.WRKPACKINGGROUP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

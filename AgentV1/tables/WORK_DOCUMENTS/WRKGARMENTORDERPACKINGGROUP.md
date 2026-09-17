# DB2ADMIN.WRKGARMENTORDERPACKINGGROUP

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 49
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 197373

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
| 8 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 9 | `PACKINGGROUP` | CHAR(15) |  |  |  |  |
| 10 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 11 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 12 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 13 | `SUBCODE02` | CHAR(20) |  |  | generic_classification_code |  |
| 14 | `SUBCODE03` | CHAR(20) |  |  | generic_classification_code |  |
| 15 | `SUBCODE04` | CHAR(20) |  |  | generic_classification_code |  |
| 16 | `SUBCODE05` | CHAR(20) |  |  | generic_classification_code |  |
| 17 | `SUBCODE06` | CHAR(20) |  |  | generic_classification_code |  |
| 18 | `SUBCODE07` | CHAR(20) |  |  | generic_classification_code |  |
| 19 | `SUBCODE08` | CHAR(20) |  |  | generic_classification_code |  |
| 20 | `SUBCODE09` | CHAR(20) |  |  | generic_classification_code |  |
| 21 | `SUBCODE10` | CHAR(20) |  |  | generic_classification_code |  |
| 22 | `COLORCODE` | CHAR(10) |  |  |  |  |
| 23 | `SIZECODE` | CHAR(10) |  |  |  |  |
| 24 | `PACKINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 25 | `LINETOEXPLODE` | INTEGER | NOT NULL |  |  |  |
| 26 | `WEIGHTNET` | DECIMAL(15,5) |  |  |  |  |
| 27 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 28 | `WEIGHTUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 29 | `TOTALCARTONS` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 30 | `TOTALPOSSIBLECARTONS` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 31 | `CARTONTOBECREATED` | DECIMAL(11,0) |  |  |  |  |
| 32 | `BALANCEQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 33 | `LENGTH` | DECIMAL(7,2) |  |  |  |  |
| 34 | `HEIGHT` | DECIMAL(7,2) |  |  |  |  |
| 35 | `WIDTH` | DECIMAL(7,2) |  |  |  |  |
| 36 | `CONTAINERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 37 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 38 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 39 | `CONTAINERELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 40 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 41 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 42 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 43 | `WEIGHTREALNET` | DECIMAL(15,5) |  |  |  |  |
| 44 | `TAREWEIGHT` | DECIMAL(15,5) |  |  |  |  |
| 45 | `DIMENSIONUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 46 | `VOLUMEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 47 | `VOLUMECONVERSIONRATE` | DECIMAL(15,5) |  |  |  |  |
| 48 | `LINKEDSIZECODE` | CHAR(10) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKGMTORDERPACKINGGROUPUID` (ABSUNIQUEID)

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
       t.LINENO,
       t.PACKINGGROUP,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE
FROM   DB2ADMIN.WRKGARMENTORDERPACKINGGROUP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

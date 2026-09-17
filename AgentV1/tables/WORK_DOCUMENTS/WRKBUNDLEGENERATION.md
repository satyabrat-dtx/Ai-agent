# DB2ADMIN.WRKBUNDLEGENERATION

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 42
- **Primary key**: `COMPANYCODE`, `PRODORDERCODE`, `CREATIONTIMESTAMP`, `ROLLNO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 128039

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PRODORDERCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 2 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 3 | `ROLLNO` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `SEQNO` | INTEGER | NOT NULL |  |  |  |
| 5 | `LAYERS` | INTEGER | NOT NULL |  |  |  |
| 6 | `DEFECTS` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 7 | `USABLE` | DECIMAL(15,5) |  |  |  |  |
| 8 | `ENDBITS` | DECIMAL(15,5) |  |  |  |  |
| 9 | `SPLITS` | INTEGER | NOT NULL |  |  |  |
| 10 | `PIECES` | INTEGER | NOT NULL |  |  |  |
| 11 | `SELECTED` | INTEGER | NOT NULL |  |  |  |
| 12 | `ROLLQTY` | DECIMAL(15,5) |  |  |  |  |
| 13 | `LAYLENGTH` | DECIMAL(15,5) |  |  |  |  |
| 14 | `MARKERCODE` | CHAR(15) |  |  |  |  |
| 15 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 16 | `ELEMENTSID` | BIGINT | NOT NULL |  |  |  |
| 17 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 18 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SHADEGROUP` | CHAR(10) |  |  |  |  |
| 28 | `COLORGROUP` | CHAR(10) |  |  |  |  |
| 29 | `COLORDESCRIPTION` | CHAR(100) |  |  |  |  |
| 30 | `PRINTGROUP` | CHAR(10) |  |  |  |  |
| 31 | `PRINTDESCRIPTION` | CHAR(100) |  |  |  |  |
| 32 | `SHRINKAGEGROUP` | CHAR(10) |  |  |  |  |
| 33 | `LOTNUM` | CHAR(35) |  |  |  |  |
| 34 | `TOBEUSEDNEXT` | DECIMAL(15,5) |  |  |  |  |
| 35 | `EXCESS` | DECIMAL(15,5) |  |  |  |  |
| 36 | `SHORTAGEMTRS` | DECIMAL(15,5) |  |  |  |  |
| 37 | `OVERLAPMTRS` | DECIMAL(15,5) |  |  |  |  |
| 38 | `DEFECTCUTS` | DECIMAL(15,5) |  |  |  |  |
| 39 | `OTHERDEFECTS` | DECIMAL(15,5) |  |  |  |  |
| 40 | `TOTALPIECES` | INTEGER | NOT NULL |  |  |  |
| 41 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKBUNDLEGENERATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PRODORDERCODE,
       t.CREATIONTIMESTAMP,
       t.ROLLNO,
       t.SEQNO,
       t.LAYERS,
       t.DEFECTS,
       t.USABLE,
       t.ENDBITS,
       t.SPLITS,
       t.PIECES,
       t.SELECTED
FROM   DB2ADMIN.WRKBUNDLEGENERATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

# DB2ADMIN.WRKQUALITYDOCUMENT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 75
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `LINE`, `SUBLINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 98286

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `SUBLINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `HEADERCODE` | CHAR(20) |  |  |  |  |
| 5 | `HEADERSUBGROUPCODE` | CHAR(5) |  |  |  |  |
| 6 | `HEADERNUMBERID` | INTEGER | NOT NULL |  |  |  |
| 7 | `HEADERLINE` | DECIMAL(15,0) |  |  |  |  |
| 8 | `HEADERDATE` | DATE |  |  |  |  |
| 9 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 10 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 11 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 12 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `LOTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 22 | `LOTCODE` | CHAR(35) |  |  |  |  |
| 23 | `ITEMELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 24 | `ITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 25 | `ITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 26 | `DEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 27 | `DEMANDCODE` | CHAR(15) |  |  |  |  |
| 28 | `ORDERPARTNERREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 29 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 30 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 31 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 32 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 33 | `CHARACTERISTICCODE` | CHAR(10) |  |  |  |  |
| 34 | `CHARACTERISTICDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 35 | `NRTEST` | INTEGER | NOT NULL |  |  |  |
| 36 | `UOMCODE` | CHAR(3) |  |  |  |  |
| 37 | `INTERNALSPECIFICATIONCODE` | CHAR(10) |  |  |  |  |
| 38 | `INTERNALSPECDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 39 | `ISOSPECIFICATIONCODE` | CHAR(10) |  |  |  |  |
| 40 | `ISOSPECDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 41 | `REPETITIONNUMBER` | INTEGER | NOT NULL |  |  |  |
| 42 | `REPETITIONPERFORMED` | INTEGER | NOT NULL |  |  |  |
| 43 | `VALUESTRING` | CHAR(50) |  |  |  |  |
| 44 | `VALUESTRINGCHECK` | SMALLINT | NOT NULL |  |  |  |
| 45 | `VALUEBOOLEAN` | SMALLINT | NOT NULL |  |  |  |
| 46 | `VALUEBOOLEANCHECK` | SMALLINT | NOT NULL |  |  |  |
| 47 | `VALUEQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 48 | `VALUEQUANTITY2` | DECIMAL(15,5) |  |  |  |  |
| 49 | `VALUEQUANTITY3` | DECIMAL(15,5) |  |  |  |  |
| 50 | `VALUEQUANTITYCHECK` | SMALLINT | NOT NULL |  |  |  |
| 51 | `SUBCODEMIN` | CHAR(50) |  |  |  |  |
| 52 | `SUBCODEMAX` | CHAR(50) |  |  |  |  |
| 53 | `SUBCODEMEDIOMIN` | CHAR(50) |  |  |  |  |
| 54 | `SUBCODEMEDIOMAX` | CHAR(50) |  |  |  |  |
| 55 | `SUBCODESTANDARD` | CHAR(50) |  |  |  |  |
| 56 | `MANDATORY` | SMALLINT | NOT NULL |  |  |  |
| 57 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 58 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 59 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 60 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 61 | `EXISTING` | SMALLINT | NOT NULL |  |  |  |
| 62 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 63 | `TESTLINESTATUS` | INTEGER | NOT NULL |  |  |  |
| 64 | `ANNOTATION` | VARCHAR(250) |  |  |  |  |
| 65 | `VALUEGROUPCODE` | CHAR(20) |  |  |  |  |
| 66 | `VALUEGROUPCHECK` | SMALLINT | NOT NULL |  |  |  |
| 67 | `GROUPCODE` | CHAR(3) |  |  |  |  |
| 68 | `ADDITIONALLINE` | SMALLINT | NOT NULL |  |  |  |
| 69 | `CANCELED` | SMALLINT | NOT NULL |  |  |  |
| 70 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 71 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 72 | `UPDATESELECTEDLINE` | SMALLINT | NOT NULL |  |  |  |
| 73 | `QUALITYREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 74 | `QUALITYREASONCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.LINE,
       t.SUBLINE,
       t.HEADERCODE,
       t.HEADERSUBGROUPCODE,
       t.HEADERNUMBERID,
       t.HEADERLINE,
       t.HEADERDATE,
       t.ITEMTYPEAFICOMPANYCODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01
FROM   DB2ADMIN.WRKQUALITYDOCUMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

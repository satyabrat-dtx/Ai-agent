# DB2ADMIN.WRKQUALITYCERTIFICATE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 76
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `LINE`, `SUBLINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 106961

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CHOOSE` | SMALLINT | NOT NULL |  |  |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 3 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 5 | `SUBLINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `IDQCERTIFICATE` | CHAR(15) |  |  |  |  |
| 7 | `VERSION` | INTEGER | NOT NULL |  |  |  |
| 8 | `DATECERTIFICATE` | DATE |  |  |  |  |
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
| 21 | `CHARACTERISTICCODE` | CHAR(10) |  |  |  |  |
| 22 | `LOTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 23 | `LOTCODE` | CHAR(35) |  |  |  |  |
| 24 | `ITEMELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 25 | `ITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 26 | `ITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 27 | `DEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 28 | `DEMANDCODE` | CHAR(15) |  |  |  |  |
| 29 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 30 | `ORDERPARTNERREQUIRED` | CHAR(1) |  |  |  |  |
| 31 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 32 | `HEADERCODE` | CHAR(20) |  |  |  |  |
| 33 | `HEADERSUBGROUPCODE` | CHAR(5) |  |  |  |  |
| 34 | `HEADERNUMBERID` | INTEGER | NOT NULL |  |  |  |
| 35 | `QACERTIFICATETYPE` | CHAR(2) |  |  |  |  |
| 36 | `HEADERLINE` | DECIMAL(7,0) |  |  |  |  |
| 37 | `HEADERDATE` | DATE |  |  |  |  |
| 38 | `VALUEBOOLEAN` | SMALLINT | NOT NULL |  |  |  |
| 39 | `VALUEMODBOOLEAN` | SMALLINT | NOT NULL |  |  |  |
| 40 | `CHARACTERISTICDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 41 | `UOMCODE` | CHAR(3) |  |  |  |  |
| 42 | `VALUESTRING` | CHAR(50) |  |  |  |  |
| 43 | `VALUEMODSTRING` | CHAR(50) |  |  |  |  |
| 44 | `ISOSPECIFICATIONCODE` | CHAR(10) |  |  |  |  |
| 45 | `VALUEQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 46 | `VALUEMODQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 47 | `VALUEQUANTITY2` | DECIMAL(15,5) |  |  |  |  |
| 48 | `VALUEQUANTITY3` | DECIMAL(15,5) |  |  |  |  |
| 49 | `INTERNALSPECIFICATIONCODE` | CHAR(10) |  |  |  |  |
| 50 | `VALUEGROUPCODE` | CHAR(20) |  |  |  |  |
| 51 | `VALUEMODGROUPCODE` | CHAR(20) |  |  |  |  |
| 52 | `DATATYPE` | CHAR(2) |  |  |  |  |
| 53 | `PRINTED` | SMALLINT | NOT NULL |  |  |  |
| 54 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 55 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 56 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 57 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 58 | `ALTERNATIVEUOMCODE` | CHAR(3) |  |  |  |  |
| 59 | `ALTERNATIVEQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 60 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 61 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 62 | `GROUPCODE` | CHAR(3) |  |  |  |  |
| 63 | `SUBCODEMIN` | CHAR(50) |  |  |  |  |
| 64 | `SUBCODEMEDIOMIN` | CHAR(50) |  |  |  |  |
| 65 | `SUBCODEMEDIOMAX` | CHAR(50) |  |  |  |  |
| 66 | `SUBCODEMAX` | CHAR(50) |  |  |  |  |
| 67 | `SUBCODESTANDARD` | CHAR(50) |  |  |  |  |
| 68 | `ALTERNATIVESUBCODEMIN` | CHAR(20) |  |  |  |  |
| 69 | `ALTERNATIVESUBCODEMEDIOMIN` | CHAR(20) |  |  |  |  |
| 70 | `ALTERNATIVESUBCODEMEDIOMAX` | CHAR(20) |  |  |  |  |
| 71 | `ALTERNATIVESUBCODEMAX` | CHAR(20) |  |  |  |  |
| 72 | `ALTERNATIVESUBCODESTANDARD` | CHAR(20) |  |  |  |  |
| 73 | `QUALITYCERTIFICATETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 74 | `TESTLINESTATUS` | INTEGER | NOT NULL |  |  |  |
| 75 | `TESTSTATUS` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CHOOSE,
       t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.LINE,
       t.SEQUENCE,
       t.SUBLINE,
       t.IDQCERTIFICATE,
       t.VERSION,
       t.DATECERTIFICATE,
       t.ITEMTYPEAFICOMPANYCODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01
FROM   DB2ADMIN.WRKQUALITYCERTIFICATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

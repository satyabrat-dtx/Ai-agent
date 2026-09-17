# DB2ADMIN.WRKDTXQUALITYDOCUMENT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 63
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 92115

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `DTXHEADERCODE` | CHAR(20) |  |  |  |  |
| 4 | `DTXHEADERSUBGROUPCODE` | CHAR(5) |  |  |  |  |
| 5 | `DTXHEADERNUMBERID` | INTEGER |  |  |  |  |
| 6 | `HEADERDATE` | DATE |  |  |  |  |
| 7 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 8 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 9 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 10 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `LOTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 20 | `LOTCODE` | CHAR(10) |  |  |  |  |
| 21 | `ITEMELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 22 | `ITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 23 | `ITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 24 | `DEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 25 | `DEMANDCODE` | CHAR(15) |  |  |  |  |
| 26 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 27 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 28 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 29 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 30 | `HEADERLINE` | DECIMAL(5,0) |  |  |  |  |
| 31 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 32 | `CHARACTERISTICCODE` | CHAR(5) |  |  |  |  |
| 33 | `CHARACTERISTICDESCRIPTION` | CHAR(50) |  |  |  |  |
| 34 | `USERGRPUOMUSERGENGRPTYPECMYCOD` | CHAR(3) |  |  |  |  |
| 35 | `USERGRPUOMUSERGENGRPTYPECODE` | CHAR(3) |  |  |  |  |
| 36 | `USERGROUPUOMCODE` | CHAR(10) |  |  |  |  |
| 37 | `NRTEST` | INTEGER | NOT NULL |  |  |  |
| 38 | `DESCRIPTIONUOM` | VARCHAR(40) |  |  |  |  |
| 39 | `USERGRPSPCUSERGENGRPTYPECMYCOD` | CHAR(3) |  |  |  |  |
| 40 | `USERGRPSPCUSERGENGRPTYPECODE` | CHAR(3) |  |  |  |  |
| 41 | `USERGROUPSPCCODE` | CHAR(10) |  |  |  |  |
| 42 | `DESCRIPTIONSPC` | VARCHAR(40) |  |  |  |  |
| 43 | `USERGRPSPIUSERGENGRPTYPECMYCOD` | CHAR(3) |  |  |  |  |
| 44 | `USERGRPSPIUSERGENGRPTYPECODE` | CHAR(3) |  |  |  |  |
| 45 | `USERGROUPSPICODE` | CHAR(10) |  |  |  |  |
| 46 | `DESCRIPTIONSPI` | VARCHAR(40) |  |  |  |  |
| 47 | `VALUESTRING` | CHAR(20) |  |  |  |  |
| 48 | `VALUESTRINGCHECK` | SMALLINT | NOT NULL |  |  |  |
| 49 | `VALUEBOOLEAN` | SMALLINT | NOT NULL |  |  |  |
| 50 | `VALUEBOOLEANCHECK` | SMALLINT | NOT NULL |  |  |  |
| 51 | `VALUEQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 52 | `VALUEQUANTITYCHECK` | SMALLINT | NOT NULL |  |  |  |
| 53 | `SUBCODEMIN` | CHAR(20) |  |  |  |  |
| 54 | `SUBCODEMAX` | CHAR(20) |  |  |  |  |
| 55 | `SUBCODEMEDIOMIN` | CHAR(20) |  |  |  |  |
| 56 | `SUBCODEMEDIOMAX` | CHAR(20) |  |  |  |  |
| 57 | `SUBCODESTANDARD` | CHAR(20) |  |  |  |  |
| 58 | `MANDATORY` | SMALLINT | NOT NULL |  |  |  |
| 59 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 60 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 61 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 62 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.LINE,
       t.DTXHEADERCODE,
       t.DTXHEADERSUBGROUPCODE,
       t.DTXHEADERNUMBERID,
       t.HEADERDATE,
       t.ITEMTYPEAFICOMPANYCODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03
FROM   DB2ADMIN.WRKDTXQUALITYDOCUMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

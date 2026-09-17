# DB2ADMIN.QAAUTOMATICGENERATIONERROR

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 34
- **Primary key**: `COMPANYCODE`, `CREATIONID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 112523

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 2 | `OPERATIONTYPE` | CHAR(2) |  |  |  |  |
| 3 | `DETAILREQUIRED` | CHAR(2) |  |  |  |  |
| 4 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 5 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
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
| 16 | `LOTCODE` | CHAR(35) |  |  |  |  |
| 17 | `ITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 18 | `ITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 19 | `DEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 20 | `DEMANDCODE` | CHAR(15) |  |  |  |  |
| 21 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 22 | `QAITEMGROUPCODE` | CHAR(10) |  |  |  |  |
| 23 | `ORDERPARTNERREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 24 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 25 | `ERRORS` | VARCHAR(960) |  |  |  |  |
| 26 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 27 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 28 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 29 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 30 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 31 | `QAITEMGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 32 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 33 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `QAAUTOMATICGENERATIONERRORUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATIONID,
       t.OPERATIONTYPE,
       t.DETAILREQUIRED,
       t.ITEMTYPEAFICOMPANYCODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06
FROM   DB2ADMIN.QAAUTOMATICGENERATIONERROR t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

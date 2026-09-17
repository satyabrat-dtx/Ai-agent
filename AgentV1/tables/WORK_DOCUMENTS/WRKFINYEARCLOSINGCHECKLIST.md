# DB2ADMIN.WRKFINYEARCLOSINGCHECKLIST

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 27
- **Primary key**: `CREATIONTIMESTAMP`, `LINENUMBER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 205735

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `LINENUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `DETAILLINENUMBER` | DECIMAL(7,0) |  |  |  |  |
| 4 | `GLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 5 | `GLCODE` | CHAR(20) |  |  |  |  |
| 6 | `SLCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 7 | `SLCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 8 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 9 | `DOCUMENTTYPECODE` | CHAR(3) |  |  |  |  |
| 10 | `DOCUMENTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 11 | `AMOUNTINDC` | DECIMAL(18,5) |  |  |  |  |
| 12 | `AMOUNTINCC` | DECIMAL(18,5) |  |  |  |  |
| 13 | `REMARK` | VARCHAR(255) |  |  |  |  |
| 14 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 15 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 16 | `FINDOCDOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 17 | `FINDOCCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 18 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 19 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 20 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 21 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 22 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 23 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 24 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 25 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 26 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFINYEARCLOSINGCHECKLISTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.LINENUMBER,
       t.DETAILLINENUMBER,
       t.GLCOMPANYCODE,
       t.GLCODE,
       t.SLCUSTOMERSUPPLIERTYPE,
       t.SLCUSTOMERSUPPLIERCODE,
       t.EXCHANGERATE,
       t.DOCUMENTTYPECODE,
       t.DOCUMENTCURRENCYCODE,
       t.AMOUNTINDC
FROM   DB2ADMIN.WRKFINYEARCLOSINGCHECKLIST t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

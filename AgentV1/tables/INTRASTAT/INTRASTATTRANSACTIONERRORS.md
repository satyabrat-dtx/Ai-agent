# DB2ADMIN.INTRASTATTRANSACTIONERRORS

- **Module**: `INTRASTAT` (high confidence — table name starts with 'INTRASTAT')
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `COMPANYCODE`, `CUSTOMERSUPPLIERTYPE`, `CUSTOMERCUSTOMERSUPPLIERCODE`, `SUPPLIERCUSTOMERSUPPLIERCODE`, `DOCUMENTDATE`, `DEFINITIVECOUNTERCODE`, `DEFINITIVECODE`, `ORIGINDOCUMENTNUMBER`, `DOCUMENTLINENUMBER`, `ERRORNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 31864

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CUSTOMERSUPPLIERTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 2 | `CUSTOMERCUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `SUPPLIERCUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 4 | `DOCUMENTDATE` | DATE | NOT NULL | PK | primary_key |  |
| 5 | `DEFINITIVECOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 6 | `DEFINITIVECODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 7 | `ORIGINDOCUMENTNUMBER` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 8 | `DOCUMENTLINENUMBER` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 9 | `ERRORNUMBER` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 10 | `ERRORCODE` | CHAR(12) | NOT NULL |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 16 | `DEFINITIVECOUNTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `INTRASTATTRANSACTIONERRORS.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `INTRASTATTRANSACTIONERRORSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CUSTOMERSUPPLIERTYPE,
       t.CUSTOMERCUSTOMERSUPPLIERCODE,
       t.SUPPLIERCUSTOMERSUPPLIERCODE,
       t.DOCUMENTDATE,
       t.DEFINITIVECOUNTERCODE,
       t.DEFINITIVECODE,
       t.ORIGINDOCUMENTNUMBER,
       t.DOCUMENTLINENUMBER,
       t.ERRORNUMBER,
       t.ERRORCODE,
       t.CREATIONDATETIME
FROM   DB2ADMIN.INTRASTATTRANSACTIONERRORS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

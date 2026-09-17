# DB2ADMIN.FINCLEARINGACTION

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `ACCOUNTAREA`, `CLEARINGPROCESS`, `PREANALYSISRESULTCODE`, `CLEARINGACTION`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 101355

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `ACCOUNTAREA` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 3 | `CLEARINGPROCESS` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 4 | `PREANALYSISRESULTCODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `CLEARINGACTION` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 6 | `LONGDESCRIPTION` | VARCHAR(100) | NOT NULL |  | description | Long human-readable label. |
| 7 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 8 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 9 | `DEFAULT` | SMALLINT | NOT NULL |  |  |  |
| 10 | `CONFIRMREQUEST` | SMALLINT | NOT NULL |  |  |  |
| 11 | `CLEARINGACTIONPOLICYCODE` | CHAR(20) |  |  |  |  |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINCLEARINGACTION.COMPANYCODE = COMPANY.CODE` |
| `FINMATCH_PREANALYSISRESULT` | `PREANALYSISRESULTCODE` | [`FINMATCH`](../FINANCE/FINMATCH.md) | `CODE` | RESTRICT | `FINCLEARINGACTION.PREANALYSISRESULTCODE = FINMATCH.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINCLEARINGACTIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ACCOUNTAREA,
       t.CLEARINGPROCESS,
       t.PREANALYSISRESULTCODE,
       t.CLEARINGACTION,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.DEFAULT,
       t.CONFIRMREQUEST,
       t.CLEARINGACTIONPOLICYCODE
FROM   DB2ADMIN.FINCLEARINGACTION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

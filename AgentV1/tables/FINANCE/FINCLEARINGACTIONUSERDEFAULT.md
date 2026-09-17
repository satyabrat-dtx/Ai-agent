# DB2ADMIN.FINCLEARINGACTIONUSERDEFAULT

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `USERUSERID`, `ACCOUNTAREA`, `CLEARINGPROCESS`, `PREANALYSISRESULTCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 101406

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `USERUSERID` | CHAR(25) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ACCOUNTAREA` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 4 | `CLEARINGPROCESS` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 5 | `PREANALYSISRESULTCODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `CLEARINGACTION` | CHAR(2) | NOT NULL |  |  |  |
| 7 | `CONFIRMREQUEST` | SMALLINT | NOT NULL |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSUSERDEF_USER` | `USERUSERID` | [`ABSUSERDEF`](../PLATFORM/ABSUSERDEF.md) | `USERID` | RESTRICT | `FINCLEARINGACTIONUSERDEFAULT.USERUSERID = ABSUSERDEF.USERID` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINCLEARINGACTIONUSERDEFAULT.COMPANYCODE = COMPANY.CODE` |
| `FINMATCH_PREANALYSISRESULT` | `PREANALYSISRESULTCODE` | [`FINMATCH`](../FINANCE/FINMATCH.md) | `CODE` | RESTRICT | `FINCLEARINGACTIONUSERDEFAULT.PREANALYSISRESULTCODE = FINMATCH.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `CLEARINGACTIONUSERDEFAULTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.USERUSERID,
       t.ACCOUNTAREA,
       t.CLEARINGPROCESS,
       t.PREANALYSISRESULTCODE,
       t.CLEARINGACTION,
       t.CONFIRMREQUEST,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.FINCLEARINGACTIONUSERDEFAULT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

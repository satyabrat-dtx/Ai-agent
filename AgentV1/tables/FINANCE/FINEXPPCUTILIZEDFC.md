# DB2ADMIN.FINEXPPCUTILIZEDFC

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `FINPACKINGCREDITCOMPANYCODE`, `FINPACKINGCREDITLETTERNO`, `FINFCNOFCNO`, `LINENUMBER`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 201802

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINPACKINGCREDITCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FINPACKINGCREDITLETTERNO` | CHAR(5) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FINFCNOFCNO` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LINENUMBER` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 4 | `UTILIZEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 9 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 10 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FINFORWARDCONTRACT_FINFCNO` | `FINPACKINGCREDITCOMPANYCODE`, `FINFCNOFCNO` | [`FINFORWARDCONTRACT`](../FINANCE/FINFORWARDCONTRACT.md) | `COMPANYCODE`, `FCNO` | RESTRICT | `FINEXPPCUTILIZEDFC.FINPACKINGCREDITCOMPANYCODE = FINFORWARDCONTRACT.COMPANYCODE AND FINEXPPCUTILIZEDFC.FINFCNOFCNO = FINFORWARDCONTRACT.FCNO` |
| `FINPACKINGCREDIT_PCUTILIZEDFC` | `FINPACKINGCREDITCOMPANYCODE`, `FINPACKINGCREDITLETTERNO` | [`FINPACKINGCREDIT`](../FINANCE/FINPACKINGCREDIT.md) | `COMPANYCODE`, `LETTERNO` | RESTRICT | `FINEXPPCUTILIZEDFC.FINPACKINGCREDITCOMPANYCODE = FINPACKINGCREDIT.COMPANYCODE AND FINEXPPCUTILIZEDFC.FINPACKINGCREDITLETTERNO = FINPACKINGCREDIT.LETTERNO` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINEXPPCUTILIZEDFCUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FINPACKINGCREDITCOMPANYCODE,
       t.FINPACKINGCREDITLETTERNO,
       t.FINFCNOFCNO,
       t.LINENUMBER,
       t.UTILIZEDAMOUNT,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.FINEXPPCUTILIZEDFC t
FETCH FIRST 100 ROWS ONLY;
```

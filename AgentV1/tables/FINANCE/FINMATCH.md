# DB2ADMIN.FINMATCH

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 22
- **Primary key**: `CODE`
- **FK degree**: referenced by 2 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 101672

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(4) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `LONGDESCRIPTION` | VARCHAR(100) | NOT NULL |  | description | Long human-readable label. |
| 2 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 3 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 4 | `DETAILNBR` | CHAR(1) | NOT NULL |  |  |  |
| 5 | `DETAILBLOCKED` | CHAR(1) | NOT NULL |  |  |  |
| 6 | `DETAILMATCHONE` | CHAR(1) | NOT NULL |  |  |  |
| 7 | `DETAILMATCHALL` | CHAR(1) | NOT NULL |  |  |  |
| 8 | `USEABLEFORCUSTOMER` | SMALLINT | NOT NULL |  |  |  |
| 9 | `USEABLEFORSUPPLIER` | SMALLINT | NOT NULL |  |  |  |
| 10 | `USEABLEFORGLACCOUNT` | SMALLINT | NOT NULL |  |  |  |
| 11 | `USEABLEWITHCLEARINGVALUE` | SMALLINT | NOT NULL |  |  |  |
| 12 | `USEABLEWITHSUBSEQUENTCLEARING` | SMALLINT | NOT NULL |  |  |  |
| 13 | `DEFAULTACTION` | CHAR(2) | NOT NULL |  |  |  |
| 14 | `OTHERACTION2` | CHAR(2) | NOT NULL |  |  |  |
| 15 | `OTHERACTION3` | CHAR(2) | NOT NULL |  |  |  |
| 16 | `OTHERACTION4` | CHAR(2) | NOT NULL |  |  |  |
| 17 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 18 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 19 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 20 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `FINMATCH_PREANALYSISRESULT` | [`FINCLEARINGACTION`](../FINANCE/FINCLEARINGACTION.md) | `PREANALYSISRESULTCODE` | `FINCLEARINGACTION.PREANALYSISRESULTCODE = FINMATCH.CODE` |
| `FINMATCH_PREANALYSISRESULT` | [`FINCLEARINGACTIONUSERDEFAULT`](../FINANCE/FINCLEARINGACTIONUSERDEFAULT.md) | `PREANALYSISRESULTCODE` | `FINCLEARINGACTIONUSERDEFAULT.PREANALYSISRESULTCODE = FINMATCH.CODE` |

## Indexes

- `FINMATCHUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.DETAILNBR,
       t.DETAILBLOCKED,
       t.DETAILMATCHONE,
       t.DETAILMATCHALL,
       t.USEABLEFORCUSTOMER,
       t.USEABLEFORSUPPLIER,
       t.USEABLEFORGLACCOUNT,
       t.USEABLEWITHCLEARINGVALUE
FROM   DB2ADMIN.FINMATCH t
FETCH FIRST 100 ROWS ONLY;
```

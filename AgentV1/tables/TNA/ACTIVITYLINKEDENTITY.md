# DB2ADMIN.ACTIVITYLINKEDENTITY

- **Module**: `TNA` (low confidence — FK neighbourhood: 1 of 1 related tables are TNA)
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `TNADETAILTNAHEADERCOMPANYCODE`, `TNADETAILTNAHEADERCODE`, `TNADETAILSEQNO`, `AUTHORIZATIONTEMPLATECODE`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 191094

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TNADETAILTNAHEADERCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `TNADETAILSEQNO` | DECIMAL(5,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `AUTHORIZATIONTEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 4 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 5 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 6 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 7 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 8 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 10 | `TNADETAILTNAHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `AUTHORIZATIONTEMPLATE_AUTHORIZATIONTEMPLATE` | `TNADETAILTNAHEADERCOMPANYCODE`, `AUTHORIZATIONTEMPLATECODE` | [`AUTHORIZATIONTEMPLATE`](../TNA/AUTHORIZATIONTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ACTIVITYLINKEDENTITY.TNADETAILTNAHEADERCOMPANYCODE = AUTHORIZATIONTEMPLATE.COMPANYCODE AND ACTIVITYLINKEDENTITY.AUTHORIZATIONTEMPLATECODE = AUTHORIZATIONTEMPLATE.CODE` |
| `TNADETAIL_LINKEDENTITY` | `TNADETAILTNAHEADERCOMPANYCODE`, `TNADETAILTNAHEADERCODE`, `TNADETAILSEQNO` | [`TNADETAIL`](../TNA/TNADETAIL.md) | `TNAHEADERCOMPANYCODE`, `TNAHEADERCODE`, `SEQNO` | RESTRICT | `ACTIVITYLINKEDENTITY.TNADETAILTNAHEADERCOMPANYCODE = TNADETAIL.TNAHEADERCOMPANYCODE AND ACTIVITYLINKEDENTITY.TNADETAILTNAHEADERCODE = TNADETAIL.TNAHEADERCODE AND ACTIVITYLINKEDENTITY.TNADETAILSEQNO = TNADETAIL.SEQNO` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ACTIVITYLINKEDENTITY_AUTHORIZEDUSERS` | [`AUTHORIZEDUSER`](../PLATFORM/AUTHORIZEDUSER.md) | `COMPANY`, `HEADERCODE`, `TNASQN`, `CODE` | `AUTHORIZEDUSER.COMPANY = ACTIVITYLINKEDENTITY.TNADETAILTNAHEADERCOMPANYCODE AND AUTHORIZEDUSER.HEADERCODE = ACTIVITYLINKEDENTITY.TNADETAILTNAHEADERCODE AND AUTHORIZEDUSER.TNASQN = ACTIVITYLINKEDENTITY.TNADETAILSEQNO AND AUTHORIZEDUSER.CODE = ACTIVITYLINKEDENTITY.AUTHORIZATIONTEMPLATECODE` |

## Indexes

- `ACTIVITYLINKEDENTITYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TNADETAILTNAHEADERCODE,
       t.TNADETAILSEQNO,
       t.AUTHORIZATIONTEMPLATECODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID,
       t.TNADETAILTNAHEADERCOMPANYCODE
FROM   DB2ADMIN.ACTIVITYLINKEDENTITY t
FETCH FIRST 100 ROWS ONLY;
```

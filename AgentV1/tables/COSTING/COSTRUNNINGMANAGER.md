# DB2ADMIN.COSTRUNNINGMANAGER

- **Module**: `COSTING` (high confidence — table name starts with 'COST')
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`
- **FK degree**: referenced by 1 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 72915

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `FORCEEVALUATIONRUN` | SMALLINT | NOT NULL |  |  |  |
| 2 | `LASTVALUATIONRUNENDEDTIME` | TIMESTAMP |  |  |  |  |
| 3 | `RUNNINGLASTUPDATINGTIME` | TIMESTAMP |  |  |  |  |
| 4 | `NEXTVALUTAIONRUN` | TIMESTAMP |  |  |  |  |
| 5 | `RUNNINGSTEP` | CHAR(1) |  |  |  |  |
| 6 | `RUNNINGVALUATIONSEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 7 | `RUNNINGDATE` | DATE |  |  |  |  |
| 8 | `RUNNINGERROR` | VARCHAR(250) |  |  |  |  |
| 9 | `ENDBLOCKDEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 10 | `ENDBLOCKDEMANDCODE` | CHAR(20) |  |  |  |  |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 12 | `SUSPENDRUNNING` | SMALLINT | NOT NULL |  |  |  |
| 13 | `FULLCYCLECALCSTARTINGTIME` | TIMESTAMP |  |  |  |  |
| 14 | `STARTCYCLEREASON` | CHAR(1) |  |  |  |  |
| 15 | `SUSPENDRUNREQUEST` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `COSTRUNNINGMANAGER_CRMHISTORY` | [`COSTRUNNINGMANAGERHISTORY`](../COSTING/COSTRUNNINGMANAGERHISTORY.md) | `COSTRUNNINGMANAGERCOMPANYCODE` | `COSTRUNNINGMANAGERHISTORY.COSTRUNNINGMANAGERCOMPANYCODE = COSTRUNNINGMANAGER.COMPANYCODE` |

## Indexes

- `COSTRUNNINGMANAGERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.FORCEEVALUATIONRUN,
       t.LASTVALUATIONRUNENDEDTIME,
       t.RUNNINGLASTUPDATINGTIME,
       t.NEXTVALUTAIONRUN,
       t.RUNNINGSTEP,
       t.RUNNINGVALUATIONSEQUENCE,
       t.RUNNINGDATE,
       t.RUNNINGERROR,
       t.ENDBLOCKDEMANDCOUNTERCODE,
       t.ENDBLOCKDEMANDCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.COSTRUNNINGMANAGER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

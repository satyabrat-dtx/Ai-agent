# DB2ADMIN.ABSREPORTDEFCUSTOMVALUE

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `ABSREPORTDEFCODE`, `COMPANYCODE`, `USERUSERID`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 21162

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSREPORTDEFCODE` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `USERUSERID` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 3 | `OUTPUTQUEUENAME` | CHAR(20) |  | FK | foreign_key |  |
| 4 | `DESCRIPTION` | VARCHAR(250) |  |  | description |  |
| 5 | `OUTPUTFORMAT` | CHAR(2) |  |  |  |  |
| 6 | `OUTPUTTYPE` | CHAR(1) |  |  |  |  |
| 7 | `RESOURCEBUNDLE` | CHAR(50) |  |  |  |  |
| 8 | `USERDESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 9 | `NRCOPIES` | INTEGER | NOT NULL |  |  |  |
| 10 | `FIXEDPARAMETERFIELDS` | VARCHAR(250) |  |  |  |  |
| 11 | `USERDATAPROPERTIES` | VARCHAR(250) |  |  |  |  |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 13 | `DOWNLOADFILENAME` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSOUTQUEUE_OUTPUTQUEUE` | `OUTPUTQUEUENAME` | [`ABSOUTQUEUE`](../PLATFORM/ABSOUTQUEUE.md) | `NAME` | RESTRICT | `ABSREPORTDEFCUSTOMVALUE.OUTPUTQUEUENAME = ABSOUTQUEUE.NAME` |
| `ABSREPORTDEF_CUSTOMVALUE` | `ABSREPORTDEFCODE` | [`ABSREPORTDEF`](../PLATFORM/ABSREPORTDEF.md) | `CODE` | RESTRICT | `ABSREPORTDEFCUSTOMVALUE.ABSREPORTDEFCODE = ABSREPORTDEF.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSREPORTDEFCUSTOMVALUEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSREPORTDEFCODE,
       t.COMPANYCODE,
       t.USERUSERID,
       t.OUTPUTQUEUENAME,
       t.DESCRIPTION,
       t.OUTPUTFORMAT,
       t.OUTPUTTYPE,
       t.RESOURCEBUNDLE,
       t.USERDESCRIPTION,
       t.NRCOPIES,
       t.FIXEDPARAMETERFIELDS,
       t.USERDATAPROPERTIES
FROM   DB2ADMIN.ABSREPORTDEFCUSTOMVALUE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

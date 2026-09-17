# DB2ADMIN.ABSUSERCOMPANY

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `ABSUSERDEFUSERID`, `COMPANYCODE`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 34529

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSUSERDEFUSERID` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DEFAULTCOMPANYFLAG` | SMALLINT | NOT NULL |  |  |  |
| 3 | `SENDEREMAIL` | CHAR(150) |  |  |  |  |
| 4 | `SENDERSMTPID` | CHAR(150) |  |  |  |  |
| 5 | `SENDERSMTPPWD` | CHAR(20) |  |  |  |  |
| 6 | `SMTPSERVERADDR` | CHAR(64) |  |  |  |  |
| 7 | `SMTPSERVERPORT` | CHAR(5) |  |  |  |  |
| 8 | `SMTPUSETLS` | INTEGER | NOT NULL |  |  |  |
| 9 | `SMTPUSEAUTH` | INTEGER | NOT NULL |  |  |  |
| 10 | `MAILSIGNATURE` | VARCHAR(250) |  |  |  |  |
| 11 | `NOTIFYOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 12 | `NOTIFYRETURNOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 13 | `RETURNRECEIPT` | INTEGER | NOT NULL |  |  |  |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 15 | `SMTPUSEUTF8` | INTEGER | NOT NULL |  |  |  |
| 16 | `SMTPCUSTOMPROPS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSCOMPANY_COMPANY` | `COMPANYCODE` | [`ABSCOMPANY`](../PLATFORM/ABSCOMPANY.md) | `CODE` | RESTRICT | `ABSUSERCOMPANY.COMPANYCODE = ABSCOMPANY.CODE` |
| `ABSUSERDEF_ALLOWEDCOMPANIES` | `ABSUSERDEFUSERID` | [`ABSUSERDEF`](../PLATFORM/ABSUSERDEF.md) | `USERID` | RESTRICT | `ABSUSERCOMPANY.ABSUSERDEFUSERID = ABSUSERDEF.USERID` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ABSUSERCOMPANY_ALLOWEDDIVISIONS` | [`ABSUSERDIVISION`](../PLATFORM/ABSUSERDIVISION.md) | `ABSUSERCOMPANYABSUSERDEFUSERID`, `ABSUSERCOMPANYCOMPANYCODE` | `ABSUSERDIVISION.ABSUSERCOMPANYABSUSERDEFUSERID = ABSUSERCOMPANY.ABSUSERDEFUSERID AND ABSUSERDIVISION.ABSUSERCOMPANYCOMPANYCODE = ABSUSERCOMPANY.COMPANYCODE` |

## Indexes

- `ABSUSERCOMPANYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSUSERDEFUSERID,
       t.COMPANYCODE,
       t.DEFAULTCOMPANYFLAG,
       t.SENDEREMAIL,
       t.SENDERSMTPID,
       t.SENDERSMTPPWD,
       t.SMTPSERVERADDR,
       t.SMTPSERVERPORT,
       t.SMTPUSETLS,
       t.SMTPUSEAUTH,
       t.MAILSIGNATURE,
       t.NOTIFYOPTIONS
FROM   DB2ADMIN.ABSUSERCOMPANY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

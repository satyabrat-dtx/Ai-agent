# DB2ADMIN.FINREVERSALVSUSERMAPPING

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `COMPANYCODE`, `BUSINESSUNITCODE`, `FROMDATE`, `USERUSERID`
- **FK degree**: referenced by 1 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 239301

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `BUSINESSUNITCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FROMDATE` | DATE | NOT NULL | PK | primary_key | Inclusive start of a validity period. |
| 3 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 4 | `USERUSERID` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 9 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 10 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSUSERDEF_USER` | `USERUSERID` | [`ABSUSERDEF`](../PLATFORM/ABSUSERDEF.md) | `USERID` | RESTRICT | `FINREVERSALVSUSERMAPPING.USERUSERID = ABSUSERDEF.USERID` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINREVERSALVSUSERMAPPING.COMPANYCODE = COMPANY.CODE` |
| `FINBUSINESSUNIT_BUSINESSUNIT` | `COMPANYCODE`, `BUSINESSUNITCODE` | [`FINBUSINESSUNIT`](../FINANCE/FINBUSINESSUNIT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINREVERSALVSUSERMAPPING.COMPANYCODE = FINBUSINESSUNIT.COMPANYCODE AND FINREVERSALVSUSERMAPPING.BUSINESSUNITCODE = FINBUSINESSUNIT.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `FINREVERSALVSUSERMAPPING_TEMPLATEDOCUMENT` | [`FINREVERSALVSTEMPLATEMAPPING`](../FINANCE/FINREVERSALVSTEMPLATEMAPPING.md) | `FINREVERSALVSUMPCOMPANYCODE`, `FINREVERSALVSUMPBUNITCODE`, `FINREVERSALVSUMAPPINGFROMDATE`, `FINREVERSALVSUMPUSERUSERID` | `FINREVERSALVSTEMPLATEMAPPING.FINREVERSALVSUMPCOMPANYCODE = FINREVERSALVSUSERMAPPING.COMPANYCODE AND FINREVERSALVSTEMPLATEMAPPING.FINREVERSALVSUMPBUNITCODE = FINREVERSALVSUSERMAPPING.BUSINESSUNITCODE AND FINREVERSALVSTEMPLATEMAPPING.FINREVERSALVSUMAPPINGFROMDATE = FINREVERSALVSUSERMAPPING.FROMDATE AND FINREVERSALVSTEMPLATEMAPPING.FINREVERSALVSUMPUSERUSERID = FINREVERSALVSUSERMAPPING.USERUSERID` |

## Indexes

- `FINREVERSALVSUSERMAPPINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.FROMDATE,
       t.TODATE,
       t.USERUSERID,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.FINREVERSALVSUSERMAPPING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

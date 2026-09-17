# DB2ADMIN.APPSALESORDER

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `COMPANYCODE`, `ORDERID`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 114256

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ORDERID` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 2 | `CREATEDBY` | CHAR(5) |  |  |  |  |
| 3 | `CURRENCY` | CHAR(10) |  |  |  |  |
| 4 | `ORDERTERMS` | CHAR(100) |  |  |  |  |
| 5 | `EXPDELIVERYDATE` | DATE |  |  |  |  |
| 6 | `ORDERDATE` | DATE |  |  |  |  |
| 7 | `TEMPLATESALESORDERTEMPLATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `COMMENTS` | CLOB(1000000) |  |  |  |  |
| 9 | `CUSTOMERID` | CHAR(10) |  |  |  |  |
| 10 | `COMMENTSIMAGE1` | BLOB(1000000) |  |  |  |  |
| 11 | `COMMENTSIMAGE2` | BLOB(1000000) |  |  |  |  |
| 12 | `DIRTYFLAG` | SMALLINT | NOT NULL |  |  |  |
| 13 | `SALESORDERUPDATED` | SMALLINT | NOT NULL |  |  |  |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `APPSALESORDERTEMPLATE_TEMPLATE` | `COMPANYCODE`, `TEMPLATESALESORDERTEMPLATECODE` | [`APPSALESORDERTEMPLATE`](../SALES/APPSALESORDERTEMPLATE.md) | `COMPANYCODE`, `SALESORDERTEMPLATECODE` | RESTRICT | `APPSALESORDER.COMPANYCODE = APPSALESORDERTEMPLATE.COMPANYCODE AND APPSALESORDER.TEMPLATESALESORDERTEMPLATECODE = APPSALESORDERTEMPLATE.SALESORDERTEMPLATECODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `APPSALESORDER_LINES` | [`APPSALESORDERLINE`](../SALES/APPSALESORDERLINE.md) | `APPSALESORDERCOMPANYCODE`, `APPSALESORDERORDERID` | `APPSALESORDERLINE.APPSALESORDERCOMPANYCODE = APPSALESORDER.COMPANYCODE AND APPSALESORDERLINE.APPSALESORDERORDERID = APPSALESORDER.ORDERID` |

## Implicit links (NOT declared in the DDL — inferred)

- child `APPSALESORDERLINEBEAN`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Indexes

- `APPSALESORDERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ORDERID,
       t.CREATEDBY,
       t.CURRENCY,
       t.ORDERTERMS,
       t.EXPDELIVERYDATE,
       t.ORDERDATE,
       t.TEMPLATESALESORDERTEMPLATECODE,
       t.COMMENTS,
       t.CUSTOMERID,
       t.COMMENTSIMAGE1,
       t.COMMENTSIMAGE2
FROM   DB2ADMIN.APPSALESORDER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
